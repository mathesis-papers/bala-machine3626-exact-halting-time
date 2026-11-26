'use strict';

function centered(label, y, size, color = C.white, opacity = 1) {
  txt(label, W / 2, y, {size, fam: F.mono, w: 700, c: color, a: opacity, align: 'center'});
}

function tape(bits, head, index = 0) {
  const width = 220;
  const start = 600;
  bits.forEach((bit, position) => {
    const cellX = start + position * width;
    const active = position === head;
    const color = active ? C.now : C.cyan;
    panel(cellX - 76, 410, 152, 150, 1, color, `CELL ${2 - position}`);
    txt(bit, cellX, 518, {size: 78, fam: F.mono, w: 700, c: color, align: 'center'});
  });
  txt('EXIT →', start + 3 * width, 495, {size: 40, fam: F.mono, w: 700, c: head < 0 ? C.now : C.dim});
  if (index) centered(`STEP ${index} / 5`, 650, 45, C.now);
}

function titleCard() {
  centered('MACHINE 3626', 252, 45, C.cyan);
  centered('TWO TRIPS, NO LASTING CHANGE', 346, 57);
  tape(['1', '1', '0'], 2);
  centered('6 → 5 STEPS       12 → 13 STEPS', 704, 48, C.now);
}

FILM.poster = () => titleCard();

SCENES.open = scene => {
  titleCard();
  centered('Count the zeros at the right edge.', 803, 38, C.white, at(scene, 1, 0.5));
};

SCENES.trace = scene => {
  centered('ONE ZERO: THE FIVE-STEP RUN', 266, 58);
  const phase = at(scene, 2, 0.7) > 0.5 ? 2 : at(scene, 1, 0.7) > 0.5 ? 1 : 0;
  const previous = phase === 0 ? 0 : phase === 1 ? 2 : 4;
  const fraction = Math.min(0.99, at(scene, phase, 3.2));
  const move = previous + (phase === 2 ? 1 : Math.min(2, Math.floor(3 * fraction)));
  const heads = [2, 1, 2, 1, 2, -1];
  const labels = ['A: start', 'A: find the first one', 'B: return to zero', 'A: temporary one', 'B: return to the mark', 'restore and cross'];
  tape(['1', '1', move === 3 || move === 4 ? '1' : '0'], heads[move], move);
  centered(labels[move], 750, 45);
};

SCENES.double = scene => {
  centered('ONE EXTRA ZERO', 237, 53, C.cyan);
  centered('enter   |   trip   |   mark   |   trip   |   erase', 407, 37);
  centered('1    +    T    +    1    +    T    +     1', 495, 53, C.now);
  centered('1 → 5 → 13 → 29', 660, 67, C.white, at(scene, 1, 0.5));
  centered('+3:   4 → 8 → 16 → 32', 758, 46, C.cyan, at(scene, 1, 0.8, 1.2));
};

SCENES.divisors = scene => {
  centered('WHICH DIVISORS OF 12 SURVIVE?', 270, 53);
  centered('1    2    4', 440, 78, C.cyan);
  centered('3    6    12  →  cancel', 560, 45, C.dim);
  centered('1 + 4 + 8 = 13', 720, 70, C.now, at(scene, 1, 0.5));
};

SCENES.close = scene => {
  centered('THE SAME COUNT ON BOTH SIDES', 285, 53, C.cyan);
  centered('4 × 2ᵏ − 3', 465, 108, C.now);
  centered('k = trailing zeros of a positive input', 612, 47);
  centered('Based on Ma and Zhang, version 3', 767, 35, C.white, at(scene, 0, 0.7, 0.5));
};
