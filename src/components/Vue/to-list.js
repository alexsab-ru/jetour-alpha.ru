const ToListMixin = {
	methods: {
		declOfNum(number, words = []) {
			return words[(number % 100 > 4 && number % 100 < 20) ? 2 : [2, 0, 1, 1, 1, 2][(number % 10 < 5) ? Math.abs(number) % 10 : 5]];
		},
		ToList(i) {
			return `ТО-${i} - ${(15000*i).toLocaleString('ru-RU')} км или ${i} ` + this.declOfNum(i, ['год', 'года', 'лет']);
		},
		outOnlyTo(i) {
			return `ТО-${i}`;
		},
	}
}

export default ToListMixin;