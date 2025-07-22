import { models as brandModels } from './brandsAndModels';

const form = document.querySelector('.js-trade-in-form');
const brandInput = form.querySelector('input[name="brand"]');
const modelInput = form.querySelector('input[name="model"]');
const datalistModels = form.querySelector('#models');

brandInput.addEventListener('input', (evt) => {
  modelInput.value = '';
  let modelsItem = brandModels.find(item => item[evt.target.value]);
  if (modelsItem) {
    let models = modelsItem[evt.target.value];
    let options = models.map(model => `<option value="${model}"></option>`);
    datalistModels.insertAdjacentHTML('beforeend', options.join(''));
  }
});


