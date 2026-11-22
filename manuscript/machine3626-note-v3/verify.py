import argparse
import hashlib
import itertools
import json
from pathlib import Path


RULES = {
    ('A', 0): (0, 1, 'A'),
    ('A', 1): (1, -1, 'B'),
    ('B', 0): (1, 1, 'A'),
    ('B', 1): (0, -1, 'B'),
}


def valuation(number):
    return (number & -number).bit_length() - 1


def decode_rules(number):
    rules = {}
    for index, (state, symbol) in enumerate([('A', 1), ('A', 0), ('B', 1), ('B', 0)]):
        digit = number // 8 ** (3 - index) % 8
        rules[state, symbol] = (digit // 2 % 2, -1 if digit % 2 else 1,
                                'AB'[digit // 4])
    return rules


def simulate(tape, start=0, stop=-1, limit=1000000, rules=RULES):
    state = 'A'
    head = start
    for count in range(1, limit + 1):
        symbol, direction, state = rules[state, tape.get(head, 0)]
        if symbol:
            tape[head] = symbol
        else:
            tape.pop(head, None)
        head += direction
        if head == stop:
            return count, state, tape
    raise AssertionError('Finite transition limit exceeded')


def divisors(number):
    return [candidate for candidate in range(1, number + 1) if number % candidate == 0]


def moebius(number):
    sign = 1
    prime = 2
    while prime * prime <= number:
        if number % prime == 0:
            number //= prime
            sign = -sign
            if number % prime == 0:
                return 0
        prime += 1
    return -sign if number > 1 else sign


def totient(number):
    result = number
    prime = 2
    while prime * prime <= number:
        if number % prime == 0:
            result -= result // prime
            while number % prime == 0:
                number //= prime
        prime += 1
    if number > 1:
        result -= result // number
    return result


def strings(maximum_length):
    return [bits for length in range(maximum_length + 1)
            for bits in itertools.product((0, 1), repeat=length)]


def check_machine(maximum):
    total_transitions = 0
    times = {}
    for number in range(1, maximum + 1):
        initial = {index: 1 for index in range(number.bit_length())
                   if number & (1 << index)}
        count, state, final = simulate(dict(initial))
        assert count == 4 * (1 << valuation(number)) - 3, number
        assert state == 'B' and final == initial, number
        total_transitions += count
        times[number] = count
    return total_transitions, times


def check_contexts():
    cases = 0
    for exponent in range(10):
        for higher in strings(3):
            block = (0,) * exponent + (1,) + higher
            for right in strings(3):
                initial = {index: symbol for index, symbol in enumerate(block) if symbol}
                initial.update({-index - 1: symbol for index, symbol in enumerate(right) if symbol})
                count, state, final = simulate(dict(initial))
                assert count == 4 * (1 << exponent) - 3
                assert state == 'B' and final == initial
                cases += 1
    return cases


def check_comparison_machines(maximum):
    assert decode_rules(3626) == RULES
    transitions = {}
    for machine in [3589, 3197]:
        rules = decode_rules(machine)
        total = 0
        for number in range(1, maximum + 1):
            initial = {index: 1 for index in range(number.bit_length())
                       if number & (1 << index)}
            count, state, final = simulate(dict(initial), rules=rules)
            expected = 2 * valuation(number) + 1 if machine == 3589 else 2 - (-1) ** number
            assert count == expected and final == initial, (machine, number)
            total += count
        transitions[str(machine)] = total
    return transitions


def check_timing_statistics(times):
    running = 0
    for number in range(1, 4097):
        running += times[number]
        expected = number + 4 * sum(2 ** (index - 1) * (number // 2 ** index)
                                    for index in range(1, number.bit_length()))
        assert running == expected
    for length in range(1, 17):
        values = [times[number] for number in range(2 ** (length - 1), 2 ** length)]
        assert sum(values) == (2 * length - 1) * len(values)
        assert max(values) == 2 ** (length + 1) - 3
    for maximum in [1, 2, 3, 31, 255, 1000, 4096, 65536]:
        for exponent in range(maximum.bit_length()):
            count = sum(times[number] == 4 * 2 ** exponent - 3
                        for number in range(1, maximum + 1))
            assert count == maximum // 2 ** exponent - maximum // 2 ** (exponent + 1)


def base_four_digits(number):
    return sum(4 ** index for index in range(number.bit_length())
               if number & (1 << index))


def partial_sum_divisor_sequence(number):
    return sum((index + 1) * 2 ** index for index in range(number.bit_length())
               if number & (1 << index))


def check_reference_prefixes(source, times):
    records = json.loads(source.read_text())
    formulas = {
        'A393210': lambda number: times[number],
        'A069517': lambda number: sum((-1) ** (factor + 1) * moebius(factor)
                                     for factor in divisors(number)),
        'A296306': lambda number: (4 ** (valuation(number) + 1) - 1) // 3,
        'A010684': lambda number: 2 - (-1) ** number,
        'A037227': lambda number: 2 * valuation(number) + 1,
        'A038712': lambda number: 2 ** (valuation(number) + 1) - 1,
        'A276391': lambda number: (2 * 4 ** valuation(number) + 1) // 3,
        'A318935': lambda number: (8 ** (valuation(number) + 1) - 1) // 7,
        'A000695': base_four_digits,
        'A006095': lambda number: 0 if number == 0 else
        (2 ** number - 1) * (2 ** (number - 1) - 1) // 3,
        'A080277': partial_sum_divisor_sequence,
    }
    assert set(records) == set(formulas)
    comparisons = {}
    for sequence, record in records.items():
        for number, expected in enumerate(record['terms'], start=record['offset']):
            assert formulas[sequence](number) == expected, (sequence, number)
        comparisons[sequence] = len(record['terms'])
    return comparisons


def check_arithmetic(maximum, times):
    mass = {}
    totients = {}
    ratio_values = {}
    digit_sum = 0
    for number in range(1, maximum + 1):
        factors = divisors(number)
        mass[number] = sum((-1) ** (factor + 1) * moebius(factor) for factor in factors)
        totients[number] = totient(number)
        exponent = valuation(number)
        expected_mass = 1 if number == 1 else (2 if number & (number - 1) == 0 else 0)
        assert mass[number] == expected_mass
        divisor_cost = sum(mass[factor] ** 2 * totients[factor] for factor in factors)
        assert divisor_cost == times[number] == 4 * (1 << exponent) - 3
        for power in range(1, 5):
            assert sum(2 * mass[factor] ** power - mass[factor] ** (power + 1)
                       for factor in factors) == 1
            signed_sum = sum(mass[factor] ** power * moebius(factor) for factor in factors)
            assert signed_sum == 1 - 2 ** power * (number % 2 == 0)
            parity_signed_sum = sum((-1) ** (factor + 1) * mass[factor] ** power
                                    * moebius(factor) for factor in factors)
            assert parity_signed_sum == 1 + 2 ** power * (number % 2 == 0)
            weight_sum = sum(mass[factor] ** power * (factor ** 3 - factor + 1)
                             for factor in factors)
            assert weight_sum == 1 + 2 ** power * sum(
                2 ** (3 * index) - 2 ** index + 1 for index in range(1, exponent + 1))
            for totient_power in range(5):
                actual = sum(mass[factor] ** power * totients[factor] ** totient_power
                             for factor in factors)
                expected = 1 + 2 ** power * sum(2 ** (totient_power * index)
                                               for index in range(exponent))
                assert actual == expected
        for power in range(5):
            numerator = sum(factor ** power for factor in factors)
            for prime in [2, 3, 5, 7]:
                reduced = number
                prime_exponent = 0
                while reduced % prime == 0:
                    reduced //= prime
                    prime_exponent += 1
                denominator = sum(factor ** power for factor in factors if factor % prime)
                assert numerator == denominator * sum(prime ** (index * power)
                                                       for index in range(prime_exponent + 1))
        assert (-1) ** (number + 1) * sum(mass[factor] ** 2 * moebius(factor)
                                         for factor in factors) == 2 + (-1) ** number
        quadratic = (2 * 4 ** exponent + 1) // 3
        assert quadratic == sum(4 ** index * (-1) ** (number // 2 ** index + 1)
                                for index in range(exponent + 1))
        assert base_four_digits(number) - base_four_digits(number - 1) == quadratic
        digit_sum += quadratic
        assert digit_sum == base_four_digits(number)
        assert (sum(times[index] for index in range(1, number + 1)) + number) // 2 == partial_sum_divisor_sequence(number)
        assert partial_sum_divisor_sequence(number) == number + 2 * partial_sum_divisor_sequence(number // 2)
        cubic = sum(factor ** 3 for factor in factors)
        odd_cubic = sum(factor ** 3 for factor in factors if factor % 2)
        assert cubic == odd_cubic * ((8 ** (exponent + 1) - 1) // 7)
        assert 1 + 4 * sum(mass[factor] * totients[factor] ** 3 for factor in factors
                           if factor > 1) == (8 ** (exponent + 1) - 1) // 7
        assert sum(mass[factor] for factor in factors) == 2 * exponent + 1
        ratio_values[number] = (4 ** (exponent + 1) - 1) // 3
    for exponent in range(1, 13):
        endpoint = 1 << exponent
        values = [ratio_values[number] for number in range(1, endpoint)]
        assert values == values[::-1]
        assert sum(values) == (endpoint - 1) * (2 * endpoint - 1) // 3
    assert mass[4] == 2 and mass[4] != 4
    return ratio_values


def main():
    parser = argparse.ArgumentParser(description='Exact finite checks for machine 3626 and divisor identities.')
    parser.add_argument('--oeis-bfile', type=Path,
                        default=Path(__file__).with_name('b393210.txt'))
    parser.add_argument('--oeis-prefix', type=Path)
    parser.add_argument('--reference-prefixes', type=Path,
                        default=Path(__file__).with_name('reference-prefixes.json'))
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    total_transitions, times = check_machine(65536)
    context_cases = check_contexts()
    comparison_transitions = check_comparison_machines(65536)
    check_timing_statistics(times)
    check_arithmetic(4096, times)
    reference_comparisons = check_reference_prefixes(arguments.reference_prefixes, times)
    comparisons = 0
    bfile_sha256 = None
    if arguments.oeis_bfile:
        source = arguments.oeis_bfile.read_bytes()
        bfile_sha256 = hashlib.sha256(source).hexdigest()
        for line in source.decode().splitlines():
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            number, expected = map(int, line.split())
            assert times[number] == expected
            comparisons += 1
        assert comparisons == 1000
    prefix_comparisons = 0
    prefix_sha256 = None
    if arguments.oeis_prefix:
        source = arguments.oeis_prefix.read_bytes()
        prefix_sha256 = hashlib.sha256(source).hexdigest()
        for line in source.decode().splitlines():
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            number, expected = map(int, line.split())
            assert times[number] == expected
            prefix_comparisons += 1
        assert prefix_comparisons > 0
    result = {
        'machine': 3626,
        'input_range': [1, 65536],
        'literal_machine_cases': 65536,
        'literal_transitions': total_transitions,
        'comparison_machine_cases_each': 65536,
        'comparison_machine_transitions': comparison_transitions,
        'tape_restoration': True,
        'context_cases': context_cases,
        'context_zero_block_lengths': [0, 9],
        'higher_and_right_context_lengths': [0, 3],
        'divisor_identity_range': [1, 4096],
        'mixed_powers': {'mass': [1, 4], 'totient': [0, 4]},
        'divisor_power_ratio_exponents': [0, 4],
        'divisor_power_ratio_primes': [2, 3, 5, 7],
        'arbitrary_weight': 'd^3-d+1, mass powers 1 through 4',
        'signed_transform_mass_powers': [1, 4],
        'indexed_parity_identity_range': [1, 4096],
        'quadratic_generating_coefficients_and_digit_sums': [1, 4096],
        'cubic_weighted_identity_range': [1, 4096],
        'corrected_support_example': {'argument': 4, 'mass': 2, 'incorrect_value': 4},
        'exact_time_prefix_sums': [1, 4096],
        'binary_lengths_mean_and_maximum': [1, 16],
        'timing_distribution_endpoints': [1, 2, 3, 31, 255, 1000, 4096, 65536],
        'palindrome_and_partial_sum_exponents': [1, 12],
        'oeis_bfile_comparisons': comparisons,
        'oeis_bfile_sha256': bfile_sha256,
        'oeis_prefix_comparisons': prefix_comparisons,
        'oeis_prefix_sha256': prefix_sha256,
        'reference_prefix_comparisons': reference_comparisons,
        'reference_prefix_sha256': hashlib.sha256(arguments.reference_prefixes.read_bytes()).hexdigest(),
        'coverage': 'Exact finite comparisons; all-input statements have written proofs in note.tex.',
        'status': 'all assertions passed',
    }
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if arguments.output:
        arguments.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
