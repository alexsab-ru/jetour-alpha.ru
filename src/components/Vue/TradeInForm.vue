<template>
	<div>
		<div class="kia-container" v-if="show">

			<div class="mb-12 flex font-medium text-cd">
				<div class="not-clickable-tab relative flex-grow flex items-center gap-4 !pt-3 border-t-4 border-t-green">
					<span class="text-black font-bold">01</span>
					<span class="text-black">Ваш автомобиль</span>
				</div>
				<div class="not-clickable-tab relative flex-grow flex items-center gap-4 !pt-3 border-t-4 border-t-black">
					<span class="text-black font-bold">02</span>
					<span class="text-black">Характеристики вашего авто</span>
				</div>
				<div class="not-clickable-tab relative flex-grow flex items-center gap-4 !pt-3 border-t border-t-cd">
					<span class="text-black font-bold">03</span>
					<span>Результаты оценки</span>
				</div>
			</div>

			<div class="mb-6">
				<p>Заполните данные о&nbsp;вашем автомобиле и&nbsp;получите предварительную оценку. <br class="hidden md:block">Вы&nbsp;можете сразу отправить ваш расчет официальному дилеру Kia и&nbsp;уточнить <br class="hidden md:block">детали выкупа автомобиля..</p>
			</div>

			<form class="mb-10">
				<h2 class="text-2xl font-bold mb-6">Введите VIN-номер</h2>
				<div class="flex">
					<input type="text" class="w-[270px] border focus:!border-black pt-2.5" placeholder="Введите VIN-номер">
					<button type="submit" class="bg-black text-white w-[42.5px] h-[42.5px] m-0 flex justify-center items-center transition-opacity hover:opacity-80"><svg data-v-134dc84b="" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid" class=""><path data-v-134dc84b="" d="M8.5 14l4-4-4-4" stroke="currentColor" stroke-width="2"></path></svg></button>
				</div>
			</form>

			<div class="flex items-end mb-8">
				<span class="flex-shrink-1 !leading-none text-9b">Или выберите из списка</span>
				<span class="flex-grow bg-cd h-[1px] ml-2"></span>
			</div>

			<nav class="trade-in-nav-tabs flex gap-6 font-medium !mb-4">
				<div class="cursor-pointer py-2 relative before:content-[''] before:absolute before:w-full before:h-[3px] before:top-0 before:bg-black before:transition-transform hover:before:scale-x-100 font-bold before:scale-x-100">Популярные</div>
				<div class="cursor-pointer py-2 relative before:content-[''] before:absolute before:w-full before:h-[3px] before:top-0 before:bg-black before:transition-transform hover:before:scale-x-100 before:scale-x-0">Все марки</div>
			</nav>

			<ul class="columns-6 space-y-2.5 font-medium mb-16">
				<li class="cursor-pointer">Acura</li>
				<li class="cursor-pointer">Alfa Romeo</li>
				<li class="cursor-pointer">Audi</li>
				<li class="cursor-pointer">BMW</li>
				<li class="cursor-pointer">Cadillac</li>
				<li class="cursor-pointer">Chery</li>
				<li class="cursor-pointer">Chevrolet</li>
				<li class="cursor-pointer">Chrysler</li>
				<li class="cursor-pointer">Citroen</li>
				<li class="cursor-pointer">Daewoo</li>
				<li class="cursor-pointer">Datsun</li>
				<li class="cursor-pointer">Dodge</li>
				<li class="cursor-pointer">DS</li>
				<li class="cursor-pointer">FAW</li>
				<li class="cursor-pointer">Fiat</li>
				<li class="cursor-pointer">Ford</li>
				<li class="cursor-pointer">Geely</li>
				<li class="cursor-pointer">Genesis</li>
				<li class="cursor-pointer">GMC</li>
				<li class="cursor-pointer">Great Wall</li>
				<li class="cursor-pointer">Haval</li>
				<li class="cursor-pointer">Honda</li>
				<li class="cursor-pointer">Hummer</li>
				<li class="cursor-pointer">Hyundai</li>
				<li class="cursor-pointer">Infiniti</li>
				<li class="cursor-pointer">Jeep</li>
				<li class="relative cursor-pointer">
					<!-- <svg width="10" height="10" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid" class="text-green absolute top-1.5 -left-4 w-2.5"><path d="M5 0l1.123 3.455h3.632L6.816 5.59 7.94 9.045 5 6.91 2.061 9.045 3.184 5.59.244 3.455h3.633L5 0z" fill="currentColor"></path></svg> -->
					Kia
					</li>
				<li class="cursor-pointer">LADA (ВАЗ)</li>
				<li class="cursor-pointer">Lamborghini</li>
				<li class="cursor-pointer">Lexus</li>
				<li class="cursor-pointer">Lifan</li>
				<li class="cursor-pointer">Mazda</li>
				<li class="cursor-pointer">Mercedes-Benz</li>
				<li class="cursor-pointer">MINI</li>
				<li class="cursor-pointer">Mitsubishi</li>
				<li class="cursor-pointer">Nissan</li>
				<li class="cursor-pointer">Opel</li>
				<li class="cursor-pointer">Peugeot</li>
				<li class="cursor-pointer">Renault</li>
				<li class="cursor-pointer">Skoda</li>
				<li class="cursor-pointer">SsangYong</li>
				<li class="cursor-pointer">Subaru</li>
				<li class="cursor-pointer">Suzuki</li>
				<li class="cursor-pointer">Toyota</li>
				<li class="cursor-pointer">Volkswagen</li>
				<li class="cursor-pointer">Volvo</li>
				<li class="cursor-pointer font-bold">
					<div class="flex items-center">
						Все марки
						<!-- <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid" class=""><path d="M8.5 14l4-4-4-4" stroke="currentColor" stroke-width="2"></path></svg> -->
					</div>
				</li>
			</ul>

			<div class="columns-6 font-medium mb-16">

				<div class="inline-block w-full mb-8">
					<span class="block text-4xl text-cd mb-3">A</span>
					<ul class="space-y-2.5">
						<li class="cursor-pointer">Acura</li>
						<li class="cursor-pointer">Alfa Romeo</li>
						<li class="cursor-pointer">Aston Martin</li>
						<li class="cursor-pointer">Audi</li>
					</ul>
				</div>
				<div class="inline-block w-full mb-8">
					<span class="block text-4xl text-cd mb-3">B</span>
					<ul class="space-y-2.5">
						<li class="cursor-pointer">Acura</li>
						<li class="cursor-pointer">Alfa Romeo</li>
						<li class="cursor-pointer">Aston Martin</li>
						<li class="cursor-pointer">Audi</li>
					</ul>
				</div>
				<div class="inline-block w-full mb-8">
					<span class="block text-4xl text-cd mb-3">C</span>
					<ul class="space-y-2.5">
						<li class="cursor-pointer">Acura</li>
						<li class="cursor-pointer">Alfa Romeo</li>
						<li class="cursor-pointer">Aston Martin</li>
						<li class="cursor-pointer">Audi</li>
					</ul>
				</div>
				<div class="inline-block w-full mb-8">
					<span class="block text-4xl text-cd mb-3">D</span>
					<ul class="space-y-2.5">
						<li class="cursor-pointer">Acura</li>
						<li class="cursor-pointer">Alfa Romeo</li>
						<li class="cursor-pointer">Aston Martin</li>
						<li class="cursor-pointer">Audi</li>
					</ul>
				</div>
				<div class="inline-block w-full mb-8">
					<span class="block text-4xl text-cd mb-3">F</span>
					<ul class="space-y-2.5">
						<li class="cursor-pointer">Acura</li>
						<li class="cursor-pointer">Alfa Romeo</li>
						<li class="cursor-pointer">Aston Martin</li>
						<li class="cursor-pointer">Audi</li>
					</ul>
				</div>
				<div class="inline-block w-full mb-8">
					<span class="block text-4xl text-cd mb-3">G</span>
					<ul class="space-y-2.5">
						<li class="cursor-pointer">Acura</li>
						<li class="cursor-pointer">Alfa Romeo</li>
						<li class="cursor-pointer">Aston Martin</li>
						<li class="cursor-pointer">Audi</li>
					</ul>
				</div>

			</div>

		</div>

		<div class="relative border-t border-t-cd overflow-hidden">
			<div class="absolute left-0 top-0 w-[33vw] bg-f8 h-full hidden sm:block"></div>

				<div class="kia-container flex flex-col-reverse sm:flex-row">

					<div class="relative w-full sm:w-1/3 sm:pr-10 py-8 sm:py-16 bg-f8 z-[1]">
						<div class="absolute -left-[5%] top-0 w-[110%] bg-f8 h-full -z-[1] block sm:hidden"></div>
						<h3 class="text-xl md:text-2xl font-bold mb-6 md:mb-8">Ваш автомобиль</h3>
						<p v-if="!brand" class="text-cd">Ничего не выбрано</p>
						<ul class="space-y-3" v-else>
							<li class="flex justify-between" v-if="brand">
								<span>Марка</span>
								<span class="flex-grow border-b border-dotted mx-2 mb-2"></span>
								<span class="font-bold" v-text="brand"></span>
							</li>
							<li class="flex justify-between" v-if="model">
								<span>Модель</span>
								<span class="flex-grow border-b border-dotted mx-2 mb-2"></span>
								<span class="font-bold" v-text="model"></span>
							</li>
							<li class="flex justify-between !mb-7" v-if="year">
								<span>Год выпуска</span>
								<span class="flex-grow border-b border-dotted mx-2 mb-2"></span>
								<span class="font-bold" v-text="year"></span>
							</li>
							<li class="flex justify-between" v-if="transmission">
								<span>Коробка передач</span>
								<span class="flex-grow border-b border-dotted mx-2 mb-2"></span>
								<span class="font-bold" v-text="transmission"></span>
							</li>
							<li class="flex justify-between" v-if="!v$.mileage.$invalid && !v$.mileage.numeric.$invalid && Number(mileage) != 0">
								<span>Пробег</span>
								<span class="flex-grow border-b border-dotted mx-2 mb-2"></span>
								<span class="font-bold" v-text="number+' км'"></span>
							</li>
						</ul>
					</div>

					<div class="w-full sm:w-2/3 sm:pl-10 py-8 sm:py-16">
						<h3 class="text-xl font-bold mb-2">Характеристики вашего авто</h3>
						<p class="mb-4">Параметры, необходимые для оценки автомобиля</p>

						<form class="vue-form grid grid-cols-6 gap-5" @submit.prevent="send">
							<input type="hidden" name="_token" :value="token">
							<input type="email" tabindex="-1" name="email" placeholder="mail@example.com">
							<input type="hidden" name="form" value="Онлайн-оценка автомобиля">
							<div class="col-span-6 lg:col-span-3 2xl:col-span-2">
								<kia-select
									placeholder="Марка автомобиля *"
									:options="brands"
									@changed="selectBrand"
									:obj="true"
									class="w-full"
									:key="key"
								/>
								<input type="hidden" name="brand" v-model="brand">
								<p
									class="text-red text-xs mt-1 mb-0"
									v-if="v$.brand.$dirty && v$.brand.required.$invalid"
								>Чтобы продолжить, выберите марку авто</p>
							</div>
							<div class="col-span-6 lg:col-span-3 2xl:col-span-2">
								<kia-select
									placeholder="Модель *"
									:options="currentModels"
									@changed="selectModel"
									:data-block="isBlock"
									class="w-full"
									:key="key"
								/>
								<input type="hidden" name="model" v-model="model">
								<p
									class="text-red text-xs mt-1 mb-0"
									v-if="v$.model.$error && v$.model.required.$invalid"
								>Чтобы продолжить, выберите модель</p>
							</div>
							<div class="col-span-6 lg:col-span-3 2xl:col-span-2">
								<kia-select
									placeholder="Год выпуска *"
									:options="years"
									@changed="selectYear"
									:data-block="isBlock"
									class="w-full"
									:key="key"
								/>
								<input type="hidden" name="year-of-issue" v-model="year">
								<p
									class="text-red text-xs mt-1 mb-0"
									v-if="v$.year.$error && v$.year.required.$invalid"
								>Чтобы продолжить, выберите год выпуска</p>
							</div>
							<kia-select
								placeholder="Коробка передач"
								:options="['Ручная', 'Автомат']"
								@changed="selectTransmission"
								:data-block="isBlock"
								class="col-span-6 lg:col-span-3 2xl:col-span-2"
								:key="key"
							/>
							<input type="hidden" name="transmission" v-model="transmission">
							<div class="col-span-6 lg:col-span-3 2xl:col-span-2">
								<input
									type="tel"
									name="mileage"
									placeholder="Пробег"
									class="!border border-cd border-solid px-2.5 focus:border-black bg-transparent col-span-6 lg:col-span-3 2xl:col-span-2"
									:class="{'border-black': mileage}"
									v-model="mileage"
									:disabled="!brand"
								>
								<p
									class="text-red text-xs mt-1 mb-0"
									v-if="v$.mileage.$invalid && v$.mileage.numeric.$invalid"
								>Доспустимы только цифры</p>
							</div>
							<div class="col-span-6 lg:col-span-3 2xl:col-span-2">
								<input
									type="tel"
									name="desiredPrice"
									placeholder="Желаемая цена"
									class="!border border-cd border-solid px-2.5 focus:border-black bg-transparent"
									:class="{'border-black': desiredPrice}"
									v-model="desiredPrice"
									:disabled="!brand"
								>
								<p
									class="text-red text-xs mt-1 mb-0"
									v-if="v$.desiredPrice.$invalid && v$.desiredPrice.numeric.$invalid"
								>Доспустимы только цифры</p>
							</div>
							<div class="col-span-6 lg:col-span-3">
								<input
									type="text"
									name="name"
									placeholder="Ваше имя"
									class="!border border-cd border-solid px-2.5 py-2 focus:border-black bg-transparent"
									:class="{'!border-black': name}"
									v-model="name"
									:disabled="!brand"
								>
							</div>
							<div class="col-span-6 lg:col-span-3">
								<input
									type="tel"
									name="phone"
									placeholder="+7 999 999-99-99 *"
									class="!border border-cd border-solid px-2.5 py-2 focus:border-black bg-transparent"
									:class="{'!border-black': phone}"
									v-model="phone"
									:disabled="!brand"
								>
								<p
									class="text-red text-xs mt-1 mb-0"
									v-if="v$.phone.$dirty && v$.phone.required.$invalid"
								>Укажите номер телефона в формате <i>+7 999 999-99-99</i></p>
								<p
									class="text-red text-xs mt-1 mb-0"
									v-if="v$.phone.$dirty && v$.phone.minLength.$invalid"
								>Минимальное количество символов</p>
							</div>
							<textarea
								placeholder="Комментарий (необязательно)"
								name="comment"
								class="!border border-cd border-solid px-2.5 py-2 focus:border-black bg-transparent h-28 resize-none col-span-6"
								:class="{'!border-black': comment}"
								v-model="comment"
								:disabled="!brand"
							></textarea>
							<button
								class="btn px-20 col-span-6 lg:col-span-3 2xl:col-span-2"
							><span>Получить&nbsp;оценку</span></button>
							<div class="col-span-6">
								<div class="flex">
									<label class="checkbox-control">
										<input
											type="checkbox"
											name="agree"
											class="agree"
											v-model="agree"
										>
										<span class="checkbox-indicator"></span>
									</label>
								<small>Проставляя отметку, Вы&nbsp;даете согласие на&nbsp;обработку Ваших персональных данных в&nbsp;соответствии с&nbsp;ФЗ &#8470;&nbsp;152 &laquo;О&nbsp;персональных данных&raquo; на&nbsp;условиях, <a href="/privacy-policy" target="_blank">указанных здесь</a>. Настоящим Вы&nbsp;выражаете свое согласие на&nbsp;получение информационных и&nbsp;рекламных материалов путем осуществления прямых контактов с&nbsp;помощью различных средств связи, включая, но, не&nbsp;ограничиваясь: почтовую рассылку, sms&nbsp;&mdash; рассылку, электронную почту, телефон, Интернет.</small>
								</div>
								<p
									class="text-red text-xs mt-1 mb-0 w-full"
									v-if="v$.agree.$error && v$.agree.sameAs.$invalid"
								>Чтобы продолжить, установите этот флажок</p>
							</div>
						</form>

					</div>

				</div>

		</div>

		<div class="sticky bottom-0 left-0 right-0 z-10 bg-white border-t border-t-cd" v-if="show">
			<div class="kia-container">
				<div class="flex justify-end">
					<div class="btn btn-white border-0 flex items-center justify-center px-20">
						<span class="flex items-center gap-1 h-5">
							<svg data-v-6e69ebae="" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid" class=""><path data-v-6e69ebae="" d="M12 5l-5 5 5 5" stroke="currentColor" stroke-width="2"></path></svg>
							Шаг назад
						</span>
					</div>
					<button class="btn px-20" @click="click"><span>Получить&nbsp;оценку</span></button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import KiaSelect from './KiaSelect.vue';
import axios from 'axios';
import { useVuelidate } from '@vuelidate/core'
import { required, sameAs, minLength, numeric } from '@vuelidate/validators'
export default {
	setup () {return { v$: useVuelidate() }},
	validations (){
		return {
			brand: { required },
			model: { required },
			year: { required },
			mileage: { numeric },
			desiredPrice: { numeric },
			phone: { required, minLength: minLength(16) },
			agree: { sameAs: sameAs(true) }
		}
	},
	mounted(){
		for(var i=1986; i<=2023; i++){
			this.years.push(i);
		}
	},
	watch: {
		phone(newVal, oldVal){
			if(newVal.length > 16){
				this.phone = oldVal;
			}
		}
	},
	methods: {
		selectBrand(id){
			if(id){
				this.currentModels = this.models[id];
				this.brands.filter(brand => {
					if(brand.id == id){
						this.brand = brand.name;
					}
				})
				this.isBlock = false;
			}
		},
		selectModel(model){this.model = model},
		selectYear(year){this.year = year},
		selectTransmission(tr){this.transmission = tr},
		getCookie(name) {
			var matches = document.cookie.match(new RegExp(
			"(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
			))
			return matches ? decodeURIComponent(matches[1]) : undefined
		},
		getPair(openURL){
			let result = {referer: window.location.origin};
			if(typeof openURL == "object") {
				openURL.search.substring(1).split('&').forEach(function(el){
					var pair = el.split('=');
					result[pair[0]] = pair[1];
				});
			}
			let source = new URL(this.getCookie('__gtm_campaign_url') ? this.getCookie('__gtm_campaign_url') : window.location);
			if(source.search != window.location.search) {
				source.search.substring(1).split('&').forEach(function(el){
					var pair = el.split('=');
					result[pair[0]] = pair[1];
				});
			}
			window.location.search.substring(1).split('&').forEach(function(el){
				var pair = el.split('=');
				result[pair[0]] = pair[1];
			});

			return result;
		},
		async send(e){
			const result = await this.v$.$validate();
			if(!result) return;
			const vm = this;
			const formData = new FormData(e.target);
			let data = this.getPair();
			Object.entries(data).forEach(function(pair){
				formData.append(pair[0], pair[1]);
			});
			formData.append(
				"page_url",
				window.location.origin + window.location.pathname
			);
			axios.post('/api/send/data', formData)
			.then(function (response) {
				window.$.magnificPopup.open({
					items: {
						src: (response.data.answer == 'ok') ? '.thanks' : '.error',
						type: 'inline'
					}
				})
				vm.brand = vm.model = vm.year = vm.transmission = vm.mileage = vm.desiredPrice = vm.name = vm.phone = vm.comment = '';
				vm.isBlock = true;
				vm.key++;
				vm.v$.$reset()
			})
			.catch(function (error) {
					console.log(error);
					window.$.magnificPopup.open({
						items: {
							src: '.error',
							type: 'inline'
						}
					})
			});
		}
	},
	computed: {
		token(){
			return document.querySelector('meta[name="csrf-token"]').content
		},
		number(){
			return Number(this.mileage).toLocaleString('ru-RU');
		}
	},
	data: () => ({
		show: false, //для скрытия неиспользуемых блоков - временно
		key: 0,
		brand: '',
		model: '',
		year: '',
		transmission: '',
		mileage: '',
		desiredPrice: '',
		name: '',
		phone: '',
		comment: '',
		agree: true,
		years: [],
		isBlock: true,
		currentModels: [],
		brands: [{"id": "2","name": "Acura"},{"id": "3","name": "Alfa Romeo"},{"id": "4","name": "Alpina"},{"id": "5","name": "Aro"},{"id": "6","name": "Asia"},{"id": "7","name": "Aston Martin"},{"id": "8","name": "Audi"},{"id": "9","name": "BAW"},{"id": "10","name": "Bentley"},{"id": "11","name": "BMW"},{"id": "12","name": "Brilliance"},{"id": "13","name": "Bufori"},{"id": "14","name": "Bugatti"},{"id": "15","name": "Buick"},{"id": "16","name": "BYD"},{"id": "17","name": "Cadillac"},{"id": "18","name": "Caterham"},{"id": "19","name": "Changan"},{"id": "20","name": "ChangFeng"},{"id": "21","name": "Chery"},{"id": "22","name": "Chevrolet"},{"id": "23","name": "Chrysler"},{"id": "24","name": "Citroen"},{"id": "25","name": "Dacia"},{"id": "26","name": "Dadi"},{"id": "27","name": "Daewoo"},{"id": "28","name": "Daihatsu"},{"id": "29","name": "Daimler"},{"id": "30","name": "Datsun"},{"id": "31","name": "Derways"},{"id": "32","name": "Dodge"},{"id": "33","name": "Dongfeng"},{"id": "34","name": "Doninvest"},{"id": "35","name": "Eagle"},{"id": "36","name": "Ecomotors"},{"id": "37","name": "FAW"},{"id": "38","name": "Ferrari"},{"id": "39","name": "FIAT"},{"id": "40","name": "Ford"},{"id": "41","name": "Geely"},{"id": "42","name": "Geo"},{"id": "43","name": "GMC"},{"id": "44","name": "Great Wall"},{"id": "45","name": "Hafei"},{"id": "46","name": "Haima"},{"id": "47","name": "Haval"},{"id": "48","name": "Hawtai"},{"id": "49","name": "Honda"},{"id": "50","name": "Huanghai"},{"id": "51","name": "Hummer"},{"id": "52","name": "Hyundai"},{"id": "53","name": "Infiniti"},{"id": "54","name": "Iran Khodro"},{"id": "55","name": "Isuzu"},{"id": "56","name": "Iveco"},{"id": "57","name": "JAC"},{"id": "58","name": "Jaguar"},{"id": "59","name": "Jeep"},{"id": "60","name": "Jinbei"},{"id": "61","name": "JMC"},{"id": "62","name": "KIA"},{"id": "63","name": "Lamborghini"},{"id": "64","name": "Lancia"},{"id": "65","name": "Land Rover"},{"id": "66","name": "Landwind"},{"id": "67","name": "LDV"},{"id": "68","name": "Lexus"},{"id": "69","name": "LIFAN"},{"id": "70","name": "Lincoln"},{"id": "71","name": "Lotus"},{"id": "72","name": "Luxgen"},{"id": "73","name": "Mahindra"},{"id": "74","name": "Marussia"},{"id": "75","name": "Maserati"},{"id": "76","name": "Maybach"},{"id": "77","name": "Mazda"},{"id": "78","name": "Mercedes-Benz"},{"id": "79","name": "Mercury"},{"id": "80","name": "Metrocab"},{"id": "81","name": "MG"},{"id": "82","name": "MINI"},{"id": "83","name": "Mitsubishi"},{"id": "84","name": "Mitsuoka"},{"id": "85","name": "Morgan"},{"id": "86","name": "Morris"},{"id": "87","name": "Nissan"},{"id": "88","name": "Noble"},{"id": "89","name": "Oldsmobile"},{"id": "90","name": "Opel"},{"id": "91","name": "Pagani"},{"id": "92","name": "Peugeot"},{"id": "93","name": "Plymouth"},{"id": "94","name": "Pontiac"},{"id": "95","name": "Porsche"},{"id": "96","name": "Proton"},{"id": "97","name": "Renault"},{"id": "98","name": "Rolls-Royce"},{"id": "99","name": "Ronart"},{"id": "100","name": "Rover"},{"id": "101","name": "Saab"},{"id": "102","name": "Saleen"},{"id": "103","name": "Saturn"},{"id": "104","name": "Scion"},{"id": "105","name": "SEAT"},{"id": "106","name": "Shuanghuan"},{"id": "107","name": "Skoda"},{"id": "108","name": "SMA"},{"id": "109","name": "Smart"},{"id": "110","name": "Spyker"},{"id": "111","name": "SsangYong"},{"id": "112","name": "Subaru"},{"id": "113","name": "Suzuki"},{"id": "114","name": "Talbot"},{"id": "115","name": "Tata"},{"id": "116","name": "Tesla"},{"id": "117","name": "Tianma"},{"id": "118","name": "Tianye"},{"id": "119","name": "Toyota"},{"id": "120","name": "Trabant"},{"id": "121","name": "Volkswagen"},{"id": "122","name": "Volvo"},{"id": "123","name": "Vortex"},{"id": "124","name": "Wartburg"},{"id": "125","name": "Wiesmann"},{"id": "126","name": "Xin Kai"},{"id": "127","name": "ZX"},{"id": "128","name": "ВАЗ (LADA)"},{"id": "129","name": "ВИС"},{"id": "130","name": "ГАЗ"},{"id": "131","name": "ЗАЗ"},{"id": "132","name": "ЗИЛ"},{"id": "133","name": "ИЖ"},{"id": "134","name": "ЛуАЗ"},{"id": "135","name": "Москвич"},{"id": "136","name": "РАФ"},{"id": "137","name": "ТагАЗ"},{"id": "138","name": "УАЗ"},{"id": "139","name": "Ravon"},{"id": "140","name": "GAC"},{"id": "141","name": "ZOTYE"},{"id": "142","name": "Foton"},{"id": "143","name": "Koenigsegg"},{"id": "144","name": "McLaren"},{"id": "145","name": "Genesis"},{"id": "146","name": "СМЗ"},{"id": "147","name": "Bajaj"},{"id": "148","name": "PUCH"},{"id": "149","name": "Westfield"},{"id": "150","name": "Zibar"},{"id": "151","name": "DS"},{"id": "152","name": "DW Hower"},{"id": "517","name": "Zuk"},{"id": "518","name": "Jonway"},{"id": "519","name": "Tatra"},{"id": "520","name": "Богдан"},{"id": "521","name": "Triumph"},{"id": "522","name": "Hanomag"},{"id": "523","name": "Barkas"},{"id": "524","name": "DeLorean"},{"id": "525","name": "Willys"},{"id": "526","name": "Changhe"},{"id": "527","name": "ЕрАЗ"},{"id": "528","name": "Lichi"},{"id": "529","name": "Leyland"},{"id": "530","name": "DKW"},{"id": "531","name": "Автокам"},{"id": "532","name": "LTI"},{"id": "533","name": "AM General"},{"id": "534","name": "Austin"},{"id": "535","name": "Nysa"},{"id": "536","name": "Zastava"},{"id": "537","name": "Renault Samsung"},{"id": "538","name": "Апал"},{"id": "539","name": "ЗиС"},{"id": "547","name": "AC"},{"id": "560","name": "CheryExeed"},{"id": "568","name": "Adler"},{"id": "569","name": "Alpine"},{"id": "570","name": "AMC"},{"id": "571","name": "Ariel"},{"id": "572","name": "Auburn"},{"id": "573","name": "Aurus"},{"id": "574","name": "Austin Healey"},{"id": "575","name": "Autobianchi"},{"id": "576","name": "BAIC"},{"id": "577","name": "Baltijas Dzips"},{"id": "578","name": "Baojun"},{"id": "579","name": "Bertone"},{"id": "580","name": "Bilenkin"},{"id": "581","name": "Bio Auto"},{"id": "582","name": "Bitter"},{"id": "583","name": "Borgward"},{"id": "584","name": "Bristol"},{"id": "585","name": "Callaway"},{"id": "586","name": "Cizeta"},{"id": "587","name": "Coggiola"},{"id": "588","name": "Cord"},{"id": "589","name": "De Tomaso"},{"id": "590","name": "Delage"},{"id": "591","name": "DeSoto"},{"id": "592","name": "Donkervoort"},{"id": "593","name": "E-Car"},{"id": "594","name": "Eagle Cars"},{"id": "595","name": "Excalibur"},{"id": "596","name": "Exeed"},{"id": "597","name": "Fisker"},{"id": "598","name": "FSO"},{"id": "599","name": "Fuqi"},{"id": "600","name": "Golden Dragon"},{"id": "601","name": "Gonow"},{"id": "602","name": "Gordon"},{"id": "603","name": "GP"},{"id": "604","name": "Graham-Paige"},{"id": "605","name": "Groz"},{"id": "606","name": "Heinkel"},{"id": "607","name": "Hindustan"},{"id": "608","name": "Hispano-Suiza"},{"id": "609","name": "Horch"},{"id": "610","name": "HSV"},{"id": "611","name": "Hudson"},{"id": "612","name": "Imperial"},{"id": "613","name": "Innocenti"},{"id": "614","name": "Invicta"},{"id": "615","name": "Isdera"},{"id": "616","name": "Jensen"},{"id": "617","name": "KTM"},{"id": "618","name": "Ligier"},{"id": "619","name": "Marcos"},{"id": "620","name": "Marlin"},{"id": "621","name": "Maruti"},{"id": "622","name": "Mega"},{"id": "623","name": "Microcar"},{"id": "624","name": "Minelli"},{"id": "625","name": "Nash"},{"id": "626","name": "NIO"},{"id": "627","name": "Osca"},{"id": "628","name": "Packard"},{"id": "629","name": "Panoz"},{"id": "630","name": "PGO"},{"id": "631","name": "Piaggio"},{"id": "632","name": "Premier"},{"id": "633","name": "Puma"},{"id": "634","name": "Qoros"},{"id": "635","name": "Qvale"},{"id": "636","name": "RAM"},{"id": "637","name": "Reliant"},{"id": "638","name": "Renaissance"},{"id": "639","name": "Rezvani"},{"id": "640","name": "Rimac"},{"id": "641","name": "Rocar"},{"id": "642","name": "Saipa"},{"id": "643","name": "Santana"},{"id": "644","name": "Simca"},{"id": "645","name": "Steyr"},{"id": "646","name": "Studebaker"},{"id": "647","name": "Tazzari"},{"id": "648","name": "Think"},{"id": "649","name": "Tramontana"},{"id": "650","name": "TVR"},{"id": "651","name": "Ultima"},{"id": "652","name": "Vauxhall"},{"id": "653","name": "Vector"},{"id": "654","name": "Venturi"},{"id": "655","name": "W Motors"},{"id": "656","name": "Wanderer"},{"id": "657","name": "Weltmeister"},{"id": "658","name": "XPeng"},{"id": "659","name": "Zenos"},{"id": "660","name": "Zenvo"},{"id": "661","name": "Канонир"},{"id": "662","name": "Комбат"},{"id": "663","name": "Руссо-Балт"},{"id": "667","name": "Voyah"},{"id": "665","name": "Neta"},{"id": "666","name": "Hongqi"},{"id": "673","name": "Amico"},{"id": "671","name": "SOL"},{"id": "672","name": "Wuling"},{"id": "678","name": "Omoda"},{"id": "675","name": "LiXiang"},{"id": "676","name": "Zeekr"},{"id": "677","name": "Skywell"},{"id": "682","name": "Denza"},{"id": "683","name": "AITO"},{"id": "687","name": "Seres"},{"id": "688","name": "Lynk & Co"},{"id": "690","name": "Cupra"},{"id": "691","name": "Tank"},{"id": "693","name": "Arcfox"},{"id": "694","name": "Evolute"},{"id": "697","name": "Panhard & Levassor"},{"id": "699","name": "Kaiyi"},{"id": "700","name": "Leapmotor"},{"id": "701","name": "Polestar"},{"id": "703","name": "Avatr"},{"id": "704","name": "Jetour"},{"id": "708","name": "Rivian"},{"id": "706","name": "Lucid"},{"id": "709","name": "Saic"},{"id": "710","name": "Sollers"},{"id": "711","name": "Roewe"},{"id": "712","name": "HiPhi"},{"id": "717","name": "Huawei"},{"id": "716","name": "Amphicar"},{"id": "718","name": "Khazar"},{"id": "781","name": "Jetta"},{"id": "788","name": "Oshan"}],
		models: {
			"1":["Ace","Aceca","Cobra","378 GT Zagato"],"2":["CL","CSX","EL","Integra","MDX","NSX","RDX","RL","RSX","SLX","TL","TLX","TSX","ZDX","ILX"],"3":["145","164","147","155","156","159","166","33","4C","75","90","Arna","Brera","Giulietta","GT","GTV","MiTo","RZ","Spider","SZ","Giulia","Stelvio","146","6C","Sprint","6","Tonale"],"4":["B10","B11","B12","B3","B5","B6","B7","B8","B9","C1","C2","D10","D3","D5","XD3","Roadster"],"5":["10","24","Spartana","Good Cat"],"6":["Hi-topic","Retona","Rocsta","Towner"],"7":["Cygnet","DB7","DB9","DBS","Lagonda","One-77","Rapide","Rapide S","V12 Vantage","V12 Vantage S","V8 Vantage","V8 Vantage S","Vanquish","Virage","DB11","DBX"],"8":["100","200","80","90","A1","A2","A3","A4","A4 Allroad Quattro","A5","A6","A6 Allroad Quattro","A7","A8","Cabriolet","Coupe","Q3","Q5","Q7","Quattro","R8","RS2","RS3","RS4","RS5","RS6","RS7","RS Q3","S1","S2","S3","S4","S5","S6","S7","S8","SQ5","TT","TT RS","TTS","V8","Q2","SQ7","Q8","Q5 Sportback","Q2L e-tron","e-tron S Sportback","RS Q3 Sportback","e-tron","e-tron GT","SQ8","e-tron Sportback","e-tron S","RS Q8","Q3 Sportback","RS e-tron GT","Q4 e-tron","SQ5 Sportback","Q5 e-tron","Q5L","Q6"],"9":["Fenix","Tonik","Land King","007"],"10":["Arnage","Azure","Bentayga","Brooklands","Continental","Continental Flying Spur","Continental GT","Continental GTC","Continental Supersports","Mulsanne","Turbo R","Flying Spur","Eight","S"],"11":["1M","1 \u0441\u0435\u0440\u0438\u044f","2 \u0441\u0435\u0440\u0438\u044f","3 \u0441\u0435\u0440\u0438\u044f","3 \u0441\u0435\u0440\u0438\u044f GT","4 \u0441\u0435\u0440\u0438\u044f","5 \u0441\u0435\u0440\u0438\u044f","5 \u0441\u0435\u0440\u0438\u044f GT","6 \u0441\u0435\u0440\u0438\u044f","7 \u0441\u0435\u0440\u0438\u044f","8 \u0441\u0435\u0440\u0438\u044f","i3","i8","M3","M4","M5","M6","X1","X3","X4","X5","X5 M","X6","X6 M","Z1","Z3","Z3 M","Z4","Z4 M","Z8","2 \u0441\u0435\u0440\u0438\u044f Active Tourer","321","4 \u0441\u0435\u0440\u0438\u044f Gran Coupe","6 \u0441\u0435\u0440\u0438\u044f Gran Coupe","M2","326","340","6 \u0441\u0435\u0440\u0438\u044f GT","X2","X7","2 \u0441\u0435\u0440\u0438\u044f Grand Tourer","8 \u0441\u0435\u0440\u0438\u044f Gran Coupe","2 \u0441\u0435\u0440\u0438\u044f Gran Coupe","327","503","M8","M8 \u0441\u0435\u0440\u0438\u044f Gran Coupe","X3 M","X4 M","E3","iX","600","i4","02 (E10)","E9","2000 C\/CS","iX3","i7","2 \u0441\u0435\u0440\u0438\u044f Gran Tourer","iX1","XM"],"12":["FRV (BS2)","H230","H530","M1 (BS6)","M2 (BS4)","M3 (BC3)","V5","V3"],"13":["La Joya","Geneva"],"14":["EB","Veyron","Chiron","T55"],"15":["Allure","Century","Electra","Enclave","Excelle","GL8","LaCrosse","LeSabre","Lucerne","Park Avenue","Rainer","Reatta","Regal","Rendezvous","Riviera","Roadmaster","Royaum","Sedan","Skylark","Terraza","Encore","Aura","Cascada","Wildcat","Special","Envision","Encore GX","Velite 6"],"16":["ET","F0","F2","F3","F6","Flyer","S8","S6","Song EV","Han EV","E6","Tang EV","Yuan","Qin Plus","Song Pro","Dolphin","Qin Pro","Song Plus","Seal","E2","Yuan Plus","Han DM"],"17":["Allante","ATS","BLS","Brougham","Catera","CTS","CTS-V","DE Ville","DTS","Eldorado","Escalade","Fleetwood","LSE","Seville","SRX","STS","Victoria","XLR","XT5","ELR","XT4\u200d","CT6","XT6","XTS","CT5","CT4"],"18":["7","21"],"19":["CS35","Eado","Raeton","CM-8","Z-Chine","Benni","CS75","CS35 Plus","CS55","UNI-K","Benben E-Star","Benni EV","Auchan X5","UNI-T","UNI-V","Auchan X7 EV","Auchan X7","CS55 Plus","CS95","CS85","Eado EV"],"20":["Flying PickUp","Flying SUV","SUV","Liebao Leopard"],"21":["A5","Amulet (A15)","Arrizo 3","Arrizo 7","Bonus (A13)","Bonus 3 (E3)","CrossEastar (B14)","Fora (A21)","IndiS (S18D)","Kimo (A1)","M11 (A3)","Oriental Son (B11)","Sweet (QQ)","QQ6 (S21)","Tiggo (T11)","Tiggo 5","Very","Tiggo 3","Tiggo 7","Tiggo 2","Tiggo 4","Tiggo 8","E5","Tiggo 7 Pro","eQ1","Tiggo 8 Pro","Eastar","eQ5","Karry","Tiggo 2 Pro","Tiggo 8 Pro Max","Tiggo E","Arrizo 5E","Tiggo 4 Pro","Tiggo 3xe","Tiggo 7 Pro Max"],"22":["Alero","Astra","Astro","Avalanche","Aveo","Bel Air","Beretta","Blazer","C10","Camaro","Caprice","Captiva","Cavalier","Celebrity","Celta","Chevette","Classic","Cobalt","Colorado","Corsa","Corsica","Corvette","Cruze","Epica","Equinox","Evanda","Express","Geo Storm","HHR","Impala","Lacetti","Lanos","Lumina","LUV D-MAX","Malibu","Metro","Monte Carlo","Monza","MW","Niva","Nubira","Omega","Orlando","Prizm","Rezzo","S10","Sail","Silverado","Sonic","Spark","SSR","Starcraft","Suburban","Tahoe","Tavera","Tracker","TrailBlazer","Trans Sport","Traverse","Uplander","Van","Vectra","Venture","Viva","Volt","Zafira","C\/K","Corvair","Blazer K5","El Camino","Cruze HR","Deluxe","Chevelle","Bolt","Lumina APV","Matiz","Nova","Sprint","Nexia","Trax","Optra","Menlo","Damas","Groove","3000 Series"],"23":["200","300C","300M","Aspen","Cirrus","Concorde","Crossfire","Daytona Shelby","Dynasty","Fifth Avenue","Grand Voyager","Imperial","Intrepid","LeBaron","LHS","Nassau","Neon","New Yorker","Pacifica","Prowler","PT Cruiser","Saratoga","Sebring","Stratus","Town & Country","Viper","Vision","Voyager","300 Letter Series","180","Simca 1308 GT","Cordoba","70 Six"],"24":["2 CV","Acadiane","Ami","AX","Berlingo","BX","C1","C15","C2","C25","C3","C35","C3 Picasso","C4","C4 Aircross","C4 Picasso","C5","C6","C8","C-Crosser","C-Elysee","CX","C-Zero","DS3","DS4","DS5","Dyane","Evasion","FAF","Grand C4 Picasso","GS","GSA","Jumper","Jumpy","LN","LNA","Mehari","Nemo","Saxo","Synergie","Visa","Xantia","XM","Xsara","Xsara Picasso","ZX","SpaceTourer","C3 Aircross","C4 SpaceTourer","Grand C4 SpaceTourer","C5 Aircross","Type H","C4 Cactus","DS","Oltcit Club","C4 X"],"25":["1304","1310","1325","1410","Dokker","Duster","Lodgy","Logan","Nova","Sandero","Solenza","Super Nova","Dokker Stepway"],"26":["City Leading","Shuttle","Smoothing"],"27":["Arcadia","Brougham","Charman","Damas","Espero","Evanda","G2X","Gentra","Istana","Kalos","Korando","Labo","Lacetti","Lanos","Leganza","LeMans","Magnus","Matiz","Musso","Nexia","Nubira","Prince","Racer","Rezzo","Sens","Statesman","Super Salon","Tacuma","Tico","Tosca","Winstorm","Lublin","Lacetti Premiere","Matiz Creative"],"28":["Altis","Applause","Atrai","Be-go","Boon","Ceria","Charade","Charmant","Coo","Copen","Cuore","Delta","Esse","Feroza","Hijet","Leeza","Materia","MAX","Mira","Move","Naked","Opti","Perodua Viva","Pyzar","Rocky","Sirion","Sonica","Storia","Taft","Tanto","Terios","Trevis","Wildcat","Xenia","YRV","Wake","Cast","Mira e:S","Terios Kid","Mebius","Hijet Truck","Hijet Caddie","Thor","Gran Move","Move Conte","Move Canbus","Boon Luminas","Tanto Exe"],"29":["Coupe","Landaulette","Limousine","Super Eight","XJ","X308"],"30":["mi-DO","on-DO","1200","Sunny","120Y","720","220C","Violet","100A\/120A"],"31":["Antelope","Aurora","Cowboy","Land Crown","Plutus","Saladin","Shuttle"],"32":["Avenger","Caliber","Caravan","Challenger","Charger","Dakota","Daytona","Durango","Dynasty","Grand Caravan","Intrepid","Journey","Magnum","Monaco","Neon","Nitro","Ram","Shadow","Spirit","Stealth","Stratus","Viper","Dart","Ram Van","Aries","Diplomat","WC series","Custom Royal","Ram Promaster City","D\/W Series"],"33":["EQ 1030","H30 Cross","MPV","Oting","Rich","S30","ZND","AX3","AX7","580","A30","AX4","M-NV","X-NV","E11K","DF6","EC35","Fengguang ix5"],"34":["Assol","Kondor","Orion"],"35":["Premier","SS","Summit","Talon","Vision"],"36":["Estrima Biro"],"37":["Admiral","Besturn","Besturn B50","Besturn B70","Besturn X80","Bora","City Golf","Jetta","Jinn","Landmark","Oley","V2","V5","Vela","Vita","Vizi","D60","Besturn X40","6350","Jumpal D60","Besturn T77","Bestune T77","Bestune NAT","Bestune T99"],"38":["208","308","328","348","360","412","456","458 Italia","458 Spider","550","575M Maranello","599 GTB Fiorano","612 Scaglietti","California","Dino","Enzo","F12berlinetta","F355","F40","F430","F50","FF","Mondial","Testarossa","Portofino","GTC4Lusso","812 Superfast","488 GTB","F8 Spider","F8 Tributo","SF90 Stradale","296 GTB","Roma","488 Pista","Purosangue"],"39":["124","126","127","131","500","600","Albea","Barchetta","Brava","Bravo","Cinquecento","Coupe","Croma","Doblo","Ducato","Duna","Fiorino","Freemont","Idea","Linea","Marea","Multipla","New 500","Palio","Panda","Punto","Regata","Ritmo","Scudo","Sedici","Seicento","Siena","Stilo","Strada","Tempra","Tipo","Ulysse","Uno","X1\/9","Fullback","Qubo","124 Spider","500L","125","Talento","Argenta","500X","124 Sport Spider"],"40":["Aerostar","Aspire","Bronco","Capri","C-MAX","Consul","Contour","Cougar","Courier","Crown Victoria","Econoline","Econovan","EcoSport","Edge","Escape","Escort","Everest","Excursion","Expedition","Explorer","F-150","F-250","F-350","Festiva","Fiesta","Fiesta ST","Five Hundred","Flex","Focus","Focus RS","Focus ST","Freestar","Freestyle","Fusion","Galaxy","Granada","Grand C-MAX","GT","Ka","Kuga","Laser","Maverick","Mondeo","Mondeo ST","Mustang","Orion","Probe","Puma","Ranger","Scorpio","Shelby","Sierra","S-MAX","Taunus","Taurus","Tempo","Thunderbird","Tourneo","Tourneo Connect","Tourneo Custom","Transit","Windstar","Fairlane","Galaxie","Transit Connect","Model A","Model T","Ranger (North America)","Spectron","Telstar","Freda","Ixion","Anglia","B-MAX","P100","Escort (North America)","Explorer Sport Trac","Fairmont","Fusion (North America)","LTD Crown Victoria","Ranchero","Transit Custom","Tourneo Courier","Torino","Model B","Territory EV","Mustang Mach-E","Custom","V8","Country Squire","Customline","Bronco Sport","Bronco II"],"41":["CK (Otaka)","Emgrand EC7","Emgrand X7","GC6","LC (Panda)","LC (Panda) Cross","Merrie","MK","MK Cross","FC (Vision)","Emgrand 7","Emgrand GT","GC9","NL-3","Atlas","Emgrand EC8","GS","LC (GC2)","Tugella","Geometry C","Atlas Pro","Coolray","Geometry A","Maple SL","Preface","Monjaro","Emgrand EV","Okavango","Jiaji"],"42":["Metro","Prizm","Spectrum","Storm","Tracker"],"43":["Acadia","Aventra","Berlina","Calais","Canyon","Caprice","Commodore","Cruze","Envoy","Jimmy","Safari","Savana","Sierra","Statesman","Suburban","Typhoon","Vandura","Yukon","Terrain","Sonoma","Hummer EV"],"44":["Coolbear","Cowry","Deer","Florid","Hover","Pegasus","Peri","Safe","Sailor","Sokol","Wingle","Voleex C10","Voleex C30","Hover H3","Hover H5","Hover H6","Hover M2","Hover M4","Sing RUV","Wingle 7","Poer"],"45":["Brio","Princip","Saibao","Sigma","Simbo"],"46":["2","3","7","M3","S5"],"47":["H1","H2","H6","H7","H8","H9","H6 Coupe","F7","F7x","H5","Jolion","Dargo","Chitu","Dargo X"],"48":["Boliger","Laville"],"49":["Accord","Airwave","Ascot","Avancier","Beat","Capa","City","Civic","Concerto","Crossroad","Crosstour","CR-V","CR-X","CR-Z","Domani","Edix","Element","Elysion","Fit","Fit Aria","FR-V","HR-V","Insight","Inspire","Integra","Jazz","Lagreat","Legend","Life","Logo","MDX","Mobilio","NSX","Odyssey","Orthia","Partner","Passport","Pilot","Prelude","Quintet","Rafaga","Ridgeline","S2000","Saber","Shuttle","SM-X","Stepwgn","Stream","That S","Today","Torneo","Vamos","Vigor","Z","Zest","Freed","Vezel","Civic Ferio","Grace","S660","Acty","Jazz AA","Fit Shuttle","Street","Integra SJ","N-One","Jade","Odyssey (North America)","Ascot Innova","Mobilio Spike","N-BOX","N-WGN","Clarity","Everus VE-1","e","Ballade","X-NV","M-NV","e:NS1","e:NP1","Crider"],"50":["Antelope","Landscape","Major","Plutus"],"51":["H1","H2","H3","HMWV \u041c-998"],"52":["Accent","Atos","Avante","Centennial","Coupe","Dynasty","Elantra","Equus","Excel","Galloper","Genesis","Getz","Grandeur","H-100","H-1 (Grand Starex)","i10","i20","i30","i40","ix20","ix35","ix55","Lantra","Lavita","Marcia","Matrix","Pony","Porter","Santa Fe","Santamo","S-Coupe","Solaris","Sonata","Starex","Stellar","Terracan","Tiburon","Trajet","Tucson","Tuscani","Veloster","Veracruz","Verna","XG","Creta","Maxcruz","Grand Santa Fe","i30 N","Kona","H-1","Grand Starex","H-200","Grace","Azera","IONIQ","Palisade","Click","Staria","IONIQ 5","Encino","Grand Creta","Bayon","Casper","Venue","Lafesta"],"53":["EX25","EX35","EX37","FX30","FX35","FX37","FX45","FX50","FX56","G20","G25","G35","G37","I30","I35","J30","JX","M25","M30","M35","M37","M45","M56","Q45","Q50","Q60","Q70","QX4","QX50","QX56","QX60","QX70","QX80","Q30","QX30","EX30","QX55"],"54":["Pars","Samand","Soren","Sahra","Tara","Dena"],"55":["Amigo","Ascender","Aska","Axiom","Bighorn","Campo","D-Max","Faster","Filly","Gemini","I-Mark","Impulse","MU","Piazza","Rodeo","Trooper","VehiCross","Wizard","Midi","Fargo","Oasis","MU-X"],"56":["Daily","Massif"],"57":["J2","J5","Refine","Rein","S5","S3","T6","iEV6","S7","J7","iEV7S","iEVS4","iEVA50","S4","JS4","JS6","T8 Pro"],"58":["E-type","F-Pace","F-type","S-type","XE","XF","XFR","XJ","XJ220","XJR","XJS","XK","XKR","XKR-S","X-type","I-Pace","E-Pace","Mark 2","Mark IX"],"59":["Cherokee","Commander","Compass","Grand Cherokee","Liberty","Patriot","Renegade","Wrangler","CJ","Gladiator","Wagoneer"],"60":["Haise"],"61":["Baodian","1032","1052"],"62":["Avella","Besta","Cadenza","Capital","Carens","Carnival","cee'd","cee'd GT","Cerato","Clarus","Concord","Enterprise","Joice","K","Magentis","Mohave","Opirus","Optima","Picanto","Potentia","Pregio","Pride","Quoris","Ray","Retona","Rio","Sedona","Sephia","Shuma","Sorento","Soul","Spectra","Sportage","Venga","Visto","X-Trek","Stinger","Bongo","Rio X-Line","Sorento Prime","Picanto X-Line","K5","K900","Towner","ProCeed","Forte","K7","Mentor","Seltos","Morning","XCeed","Rio X","K3","K9","Niro","Telluride","EV6","Lotze","K8","Stonic","KX3"],"63":["Aventador","Countach","Diablo","Espada","Gallardo","Huracan","Jalpa","LM002","Murcielago","Reventon","Veneno","Urus"],"64":["Dedra","Delta","Fulvia","Kappa","Lybra","Musa","Phedra","Prisma","Thema","Thesis","Trevi","Ypsilon","Zeta","Voyager"],"65":["Defender","Discovery","Discovery Sport","Freelander","Range Rover","Range Rover Evoque","Range Rover Sport","Series III","Range Rover Velar","MGF"],"66":["Fashion","Forward","SUV","X5","X6","X7","X8","X9"],"67":["Maxus","Convoy"],"68":["CT","ES","GS","GX","HS","IS","IS F","LFA","LS","LX","NX","RC","RX","SC","GS F","RC F","LC","UX","LM","RZ"],"69":["Breez (520)","Cebrium (720)","Celliya (530)","Smily (320)","Solano","X50","X60","Myway","\u042580","Murman","X70"],"70":["Aviator","Blackwood","Continental","LS","Mark","Mark LT","MKX","MKZ","Navigator","Town Car","Zephyr","Mark VII","Mark VIII","MKC","MKS","MKT","Nautilus","Corsair"],"71":["Eclat","Elan","Elise","Elise S","Elite","Esprit","Europa","Evora","Evora S","Excel","Exige","Exige S","Europa S","Eletre"],"72":["5 Sedan","7 MPV","7 SUV","U7 Turbo"],"73":["Armada","CJ","Commander","Marshal"],"74":["B1","B2","F2"],"75":["228","3200 GT","4300 GT Coupe","Barchetta Stradale","Biturbo","Bora","Chubasco","Coupe","Ghibli","GranCabrio","GranSport","GranTurismo","Indy","Karif","Khamsin","Kyalami","MC12","Merak","Mexico","Quattroporte","Royale","Shamal","Spyder","Levante","4200 GT","Grecale"],"76":["57","57S","62","62S"],"77":["1000","121","1300","2","3","323","3 MPS","5","6","616","626","6 MPS","818","929","Atenza","Axela","AZ-Wagon","Biante","Bongo","B-Series","BT-50","Capella","Carol","Clef","Cronos","CX-3","CX-5","CX-7","CX-9","Demio","Efini","Eunos","Eunos Cosmo","Familia","Lantis","Laputa","Levante","Luce","Millenia","MPV","MX-3","MX-5","MX-6","Navajo","Premacy","Proceed","Protege","Revue","Roadster","Rustler","RX-7","RX-8","Scrum","Sentia","Spiano","Tribute","Vantrend","Verisa","Xedos 6","Xedos 9","CX-8","Proceed Marvie","Bongo Friendee","Flair","AZ-Offroad","Bongo Brawny","Autozam AZ-3","Eunos 500","Persona","Etude","Eunos 100","Flair Crossover","Chantez","Efini MS-6","Proceed Levante","Cosmo","R360","Efini MS-8","Autozam AZ-1","Eunos 800","Flair Wagon","CX-30","MX-30","Efini MS-9","Eunos 300","CX-4","Eunos Presso","CX-60","CX-50","CX-90"],"78":["190 (W201)","AMG GT","A-\u043a\u043b\u0430\u0441\u0441","A-\u043a\u043b\u0430\u0441\u0441 AMG","B-\u043a\u043b\u0430\u0441\u0441","Citan","CLA-\u043a\u043b\u0430\u0441\u0441","CLA-\u043a\u043b\u0430\u0441\u0441 AMG","CLC-\u043a\u043b\u0430\u0441\u0441","CLK-\u043a\u043b\u0430\u0441\u0441","CLK-\u043a\u043b\u0430\u0441\u0441 AMG","SLC-\u043a\u043b\u0430\u0441\u0441","SLC-\u043a\u043b\u0430\u0441\u0441 AMG","CL-\u043a\u043b\u0430\u0441\u0441","CL-\u043a\u043b\u0430\u0441\u0441 AMG","C-\u043a\u043b\u0430\u0441\u0441","C-\u043a\u043b\u0430\u0441\u0441 AMG","E-\u043a\u043b\u0430\u0441\u0441","E-\u043a\u043b\u0430\u0441\u0441 AMG","GLA-\u043a\u043b\u0430\u0441\u0441","GLA-\u043a\u043b\u0430\u0441\u0441 AMG","GLC-\u043a\u043b\u0430\u0441\u0441","GLE-\u043a\u043b\u0430\u0441\u0441","GLE-\u043a\u043b\u0430\u0441\u0441 AMG","GLK-\u043a\u043b\u0430\u0441\u0441","GLS-\u043a\u043b\u0430\u0441\u0441","GLS-\u043a\u043b\u0430\u0441\u0441 AMG","GL-\u043a\u043b\u0430\u0441\u0441","GL-\u043a\u043b\u0430\u0441\u0441 AMG","G-\u043a\u043b\u0430\u0441\u0441","G-\u043a\u043b\u0430\u0441\u0441 AMG","Maybach S-\u043a\u043b\u0430\u0441\u0441","M-\u043a\u043b\u0430\u0441\u0441","M-\u043a\u043b\u0430\u0441\u0441 AMG","Pullman","R-\u043a\u043b\u0430\u0441\u0441","R-\u043a\u043b\u0430\u0441\u0441 AMG","SLK-\u043a\u043b\u0430\u0441\u0441","SLK-\u043a\u043b\u0430\u0441\u0441 AMG","SLR McLaren","SLS-\u043a\u043b\u0430\u0441\u0441","SLS-\u043a\u043b\u0430\u0441\u0441 AMG","SL-\u043a\u043b\u0430\u0441\u0441","SL-\u043a\u043b\u0430\u0441\u0441 AMG","Sprinter","Sprinter Classic","S-\u043a\u043b\u0430\u0441\u0441","S-\u043a\u043b\u0430\u0441\u0441 AMG","Vaneo","Vario","Viano","Vito","V-\u043a\u043b\u0430\u0441\u0441","W123","W124","GLC-\u043a\u043b\u0430\u0441\u0441 AMG","E-\u043a\u043b\u0430\u0441\u0441 All-Terrain","X-\u043a\u043b\u0430\u0441\u0441","CLS-\u043a\u043b\u0430\u0441\u0441","CLS-\u043a\u043b\u0430\u0441\u0441 AMG","GLC-\u043a\u043b\u0430\u0441\u0441 AMG Coupe","GLC-\u043a\u043b\u0430\u0441\u0441 Coupe","GLE-\u043a\u043b\u0430\u0441\u0441 AMG Coupe","GLE-\u043a\u043b\u0430\u0441\u0441 Coupe","T1","MB100","W120","W136","W108","W110","190 SL","W111","W114","W189","W115","T2","W128","W188","GLB-\u043a\u043b\u0430\u0441\u0441","W186","EQC","Simplex","W100","EQA","Maybach GLS-\u043a\u043b\u0430\u0441\u0441","GLB-\u043a\u043b\u0430\u0441\u0441 AMG","EQV","EQS","Metris","EQS AMG","220 (W187)","EQE","W29","EQE AMG","W105","W180","EQB","EQS SUV"],"79":["Capri","Cougar","Grand Marquis","Marauder","Mariner","Marquis","Milan","Montego","Monterey","Mountaineer","Mystique","Sable","Topaz","Tracer","Villager","Comet"],"80":["Taxi"],"81":["F","TF","XPower SV","ZR","ZS","ZT","550","MGB","350","3 Cross","Mulan","6"],"82":["Cooper","Cooper Clubman","Cooper Clubvan","Cooper Countryman","Cooper Paceman","Cooper S","Cooper S Clubman","Cooper S Countryman","Cooper S Paceman","John Cooper Works","John Cooper Works Clubman","John Cooper Works Countryman","John Cooper Works Paceman","One","One Clubman","One Clubvan","One Countryman","Cooper SD Countryman","Cooper SE","Cooper SE Countryman","Cooper SD Clubman"],"83":["3000 GT","Airtrek","Aspire","ASX","Carisma","Celeste","Challenger","Chariot","Colt","Cordia","Debonair","Delica","Diamante","Dingo","Dion","Eclipse","EK Wagon","Emeraude","Endeavor","Eterna","Expo LRV","FTO","Galant","Grandis","GTO","i","i-MiEV","Jeep","L200","Lancer","Lancer Evolution","Legnum","Libero","Minica","Minicab","Mirage","Montero","Montero Sport","Outlander","Pajero","Pajero Junior","Pajero Mini","Pajero Pinin","Pajero Sport","Pistachio","Proudia","Raider","RVR","Santamo","Sapporo","Sigma","Space Gear","Space Runner","Space Star","Space Wagon","Starion","Toppo","Town BOX","Tredia","Eclipse Cross","Xpander","Pajero iO","Delica D5","Delica D3","Delica D2","L300","L400","Lancer Cargo","EK Space","Strada","EK Custom","Lancer Cedia","Lancer Ralliart","EK Sport","Triton","Attrage","Xpander Cross","Outlander Sport","Minicab MiEV"],"84":["Galue","Le-Seyde","Nouera","Ryoga"],"85":["Aero","Plus 4","Plus 8","V6"],"86":["Marina"],"87":["100NX","180SX","200SX","240SX","280ZX","300ZX","350Z","370Z","AD","Almera","Almera Classic","Altima","Armada","Avenir","Bassara","Bluebird","Cedric","Cefiro","Cherry","Cima","Clipper","Crew","Cube","Datsun","Elgrand","Expert","Fairlady","Figaro","Frontier","Fuga","Gloria","GT-R","Juke","King Cab","Kix","Lafesta","Langley","Largo","Laurel","Leaf","Leopard","Liberty","Lucino","March","Maxima","Micra","Mistral","Moco","Murano","Navara","Note","NP300","NX Coupe","Otti","Pathfinder","Patrol","Pick UP","Prairie","Presage","Presea","President","Primera","Pulsar","Qashqai","Qashqai+2","Quest","Rasheen","R Nessa","Rogue","Safari","Sentra","Serena","Silvia","Skyline","Stagea","Stanza","Sunny","Teana","Terrano","Tiida","Tino","Titan","Vanette","Versa","Wingroad","X-Terra","X-Trail","NV200","Almera Tino","Auster","Dayz","Bluebird Sylphy","Caravan","Dualis","NV350 Caravan","Pixo","Primastar","Interstar","Kubistar","Urvan","Pino","Latio","Homy","S-Cargo","Dayz Roox","Roox","Sunny California","Terrano II","Tiida Latio","Trade","Vanette Cargo","NV300","Kicks","Violet","Cabstar","NV100 Clipper","Rogue Sport","Sylphy Zero Emission","Liberta Villa","e-NV200","Ariya"],"88":["M10","M12","M14","M15","M400","M600"],"89":["Achieva","Alero","Aurora","Bravada","Cutlass","Eighty-Eight","Intrigue","Ninety-Eight","Silhouette","Cutlass Supreme","Toronado","Cutlass Ciera","Omega"],"90":["Admiral","Agila","Antara","Ascona","Astra","Astra GTC","Astra OPC","Calibra","Campo","Combo","Commodore","Corsa","Corsa OPC","Diplomat","Frontera","GT","Insignia","Insignia OPC","Kadett","Manta","Meriva","Mokka","Monterey","Monza","Movano","Omega","Rekord","Senator","Signum","Sintra","Speedster","Tigra","Vectra","Vita","Vivaro","Zafira","Ampera","Kapitan","Crossland X","Grandland X","Astra Family","Vectra OPC","Zafira OPC","Olympia","Super 6","Bedford","Meriva OPC","Zafira Life","Adam Rocks","Arena","Adam","Crossland","Karl","P4","Combo Life","Cascada"],"91":["Huayra","Zonda"],"92":["1007","104","106","107","2008","204","205","206","207","208","3008","301","304","305","306","307","308","309","4007","4008","504","604","407","408","5008","505","508","605","607","806","807","Bipper","Boxer","Expert","Partner","RCZ","Traveller","405","406","J5","203","J9","404","Rifter"],"93":["Acclaim","Breeze","Caravelle","Grand Voyager","Laser","Neon","Prowler","Sundance","Voyager","Fury","Valiant","Reliant"],"94":["6000","Aztec","Bonneville","Fiero","Firebird","G4","G5","G6","G8","Grand AM","Grand Prix","GTO","LeMans","Montana","Parisienne","Phoenix","Solstice","Sunbird","Sunfire","Tempest","Torrent","Trans Sport","Vibe","Aztek","Catalina","Laurentian","Sunrunner"],"95":["356","911 Carrera","911 Carrera 4","911 Carrera 4S","911 Carrera S","911 GT2","911 GT2 RS","911 GT3","911 GT3 RS","911 GT3 RS 4.0","911 Targa 4","911 Targa 4S","911 Turbo","911 Turbo S","914","918 Spyder","924","928","944","959","968","Boxster","Boxster S","Boxster Spyder","Carrera GT","Cayenne","Cayenne GTS","Cayenne S","Cayenne Turbo","Cayenne Turbo S","Cayman","Cayman S","Macan S","Macan Turbo","Panamera","Panamera 4","Panamera 4S","Panamera GTS","Panamera S","Panamera Turbo","Panamera Turbo S","718 Boxster","718 Boxster S","718 Cayman","718 Cayman S","Macan","Macan GTS","Cayenne Coupe","Cayman GTS","Taycan","Cayman GT4","911 Speedster","Taycan Cross Turismo","911 Carrera GTS","911 Carrera 4 GTS","911 Targa 4 GTS","Taycan Sport Turismo"],"96":["Juara","Perdana","Persona","Saga","Saloon","Waja","400 Series","Putra","Satria"],"97":["11","21","14","15","16","17","18","19","20","25","30","4","5","6","9","Avantime","Clio","Clio RS","Duster","Espace","Estafette","Fluence","Fuego","Grand Scenic","Kangoo","Kaptur","Koleos","Laguna","Latitude","Logan","Master","Medallion","Megane","Megane RS","Modus","Rapid","Rodeo","Safrane","Sandero","Sandero Stepway","Scenic","Sport Spider","Super 5","Symbol","Trafic","Twingo","Twizy","Vel Satis","Wind","Dokker","12","Logan Stepway","Talisman","Kadjar","Arkana","Dokker Stepway","Captur","Grand Espace","Vel SMTis","ZOE","Dokker Van","Primaquatre","Lodgy","City K-ZE","Megane E-Tech"],"98":["Corniche Cabrio","Ghost","Park Ward","Phantom","Silver Seraph","Silver Spur","Wraith","Cullinan","Silver Shadow","Silver Spirit","Silver Cloud","20\/25","Dawn","Silver Wraith","Corniche"],"99":["Lightning"],"100":["100","200","25","400","45","600","75","800","Maestro","MGF","Mini MK","Montego","Streetwise","SD1"],"101":["90","900","9000","9-2X","9-3","9-4X","9-5","96","9-7X","99","Lancia 600"],"102":["S7"],"103":["Astra","Aura","ION","SL","LW","Outlook","Relay","SC","Sky","SW","VUE","LS"],"104":["tC","xA","xB","xD","iA"],"105":["Alhambra","Altea","Altea Freetrack","Altea XL","Arosa","Cordoba","Exeo","Fura","Ibiza","Ibiza FR","Leon","Leon FR","Malaga","Marbella","Mii","Ronda","Terra","Toledo","Ateca","Arona","Leon X-PERIENCE","Inca","Leon Cupra","Ibiza Cupra","Tarraco"],"106":["Sceo"],"107":["Citigo","Fabia","Fabia RS","Fabia Scout","Favorit","Felicia","Octavia","Octavia RS","Octavia Scout","Praktik","Rapid","Roomster","Roomster Scout","Superb","Yeti","Kodiaq","Karoq","Popular","105","100","Forman","Scala","Kodiaq RS","Kamiq"],"108":["C32","C51","C52","C61","C81","C31"],"109":["Crossblade","Forfour","Fortwo","Roadster"],"110":["C8","C12"],"111":["Actyon","Actyon Sports","Chairman","Korando Family","Istana","Kallista","Korando","Korando Sports","Kyron","Musso","Rexton","Rodius","Stavic","Tivoli","Tivoli XLV","Korando Turismo","Rexton Sports","Torres","Nomad"],"112":["Alcyone","Baja","Bistro","BRZ","Dex","Dias","Domingo","Exiga","Forester","Impreza","Justy","Legacy","Leone","Libero","Lucra","Outback","Pleo","R1","R2","Sambar","Stella","SVX","Traviq","Trezia","Tribeca","Vivio","WRX","WRX STI","XT","XV","Ascent","Legacy Lancaster","Levorg","Pleo Plus","Rex","Impreza WRX STI","Chiffon","Crosstrek","Solterra"],"113":["Aerio","Alto","Baleno","Cappuccino","Cervo","Cultus Wagon","Escudo","Every","Every Landy","Forenza","Grand Escudo","Grand Vitara","Ignis","Jimny","Kei","Kizashi","Liana","MR Wagon","Reno","Samurai","Sidekick","Splash","Swift","SX4","Verona","Vitara","Wagon R","X-90","XL7","Solio","LJ 80","Hustler","Carry","Chevrolet Cruze","Esteem","Spacia","Cultus","Equator","Landy","Palette","Swift (Japan)","Wagon R Solio","LJ 50","XBee","Twin","Cara","Alto Lapin","Wagon R Wide","Ertiga","Ciaz","S-Presso","DZire"],"114":["Alpine","Avenger","Express","Horizon","Matra Bagheera","Minx","Murena","Rancho","Rapier","Samba","Simca","Solara","Tagora"],"115":["Aria","Estate","Indica","Indigo","Mint","Safari","Sierra","Sumo","Telcoline","Xenon"],"116":["Model S","Roadster","Model 3","Model X","Model Y"],"117":["Century","Dragon"],"118":["Admiral"],"119":["4Runner","Allex","Allion","Alphard","Altezza","Aristo","Aurion","Auris","Avalon","Avensis","Aygo","bB","Belta","Blade","Blizzard","Brevis","Caldina","Cami","Camry","Carina","Cavalier","Celica","Celsior","Century","Chaser","Corolla","Corona","Corsa","Cressida","Cresta","Crown","Curren","Cynos","Duet","Echo","Estima","FJ Cruiser","Fortuner","Funcargo","Gaia","Grand Hiace","Granvia","GT 86","Harrier","Hiace","Highlander","Hilux","Innova","Ipsum","iQ","Isis","Ist","Kluger","Land Cruiser","Land Cruiser Prado","Lite Ace","Mark II","Mark X","Mark X ZiO","MasterAce","Matrix","Mega Cruiser","MR2","MR-S","Nadia","Noah","Opa","Origin","Paseo","Passo","Passo Sette","Picnic","Platz","Porte","Premio","Previa","Prius","Probox","Progres","Pronard","Ractis","Raum","RAV4","Regius","Rush","SAI","Scepter","Sequoia","Sera","Sienna","Sienta","Soarer","Solara","Soluna","Sparky","Sprinter","Sprinter Carib","Starlet","Succeed","Supra","Tacoma","Tercel","Town Ace","Tundra","Urban Cruiser","Vellfire","Venza","Verossa","Verso","Vios","Vista","Vitz","Voltz","Voxy","WiLL","Windom","Wish","Yaris","C-HR","Corolla Fielder","Spade","Camry Solara","Carina E","Carina ED","Corolla Spacio","Corolla Verso","Corona EXiV","Hilux Surf","Sprinter Marino","Sprinter Trueno","Aqua","Classic","Crown Majesta","Corolla Axio","Vanguard","Pixis Space","Pixis Epoch","Coms","ProAce","Corolla Rumion","Prius Alpha","Avensis Verso","Corolla Ceres","Corolla Runx","WiLL Cypha","Tank","Corolla Levin","Prius V","Vista Ardeo","Camry Gracia","Corolla II","Estima Lucida","Model F","Pixis Van","Comfort","Corona Premio","Esquire","Lite Ace Noah","Mark II Wagon Qualis","Prius C","Prius PHV","Regius Ace","Town Ace Noah","Roomy","Mirai","Pixis Mega","Mark II Wagon Blit","Hiace Regius","Avanza","Touring Hiace","Yaris Verso","Raize","T100","Corolla Sporty","Corolla Cross","Yaris Cross","Camry US Market","Pixis Joy","Levin"],"120":["1.1","P601"],"121":["Amarok","Beetle","Bora","Caddy","California","Caravelle","Corrado","Crafter","CrossPolo","Derby","Eos","Fox","Golf","Golf Country","Golf GTI","Golf Plus","Golf R","Iltis","Jetta","Kaefer","Lupo","Multivan","New Beetle","Passat","Passat CC","Phaeton","Pointer","Polo","Touran","Santana","Scirocco","Sharan","Taro","Tiguan","Touareg","Transporter","Up","Vento","Atlas","Arteon","LT","Routan","T-Roc","Teramont","Type 1","EuroVan","Golf R32","181","Polo GTI","Type 2","Gol","K70","Passat (North America)","Type 4","Type 166","ID.3","Touran Cross","e-Bora","Lavida","Taos","SpaceFox","ID.4","Atlas Cross Sport","ID.5","ID.6","Tiguan Allspace","ID.6 Crozz","Tiguan X","ID.4 Crozz","ID.Buzz","Phideon","Viloran","Tayron","Talagon","Arteon R","T-Cross","Tayron X","Teramont X","ID.4 X","Magotan","ID.6 X","Tharu"],"122":["140","164","240","260","340","360","440","460","480","66","740","760","780","850","940","960","C30","C70","Laplander","S40","S60","S70","S80","S90","V40","V40 Cross Country","V50","V60","V70","V90","XC60","XC70","XC90","V60 Cross Country","V90 Cross Country","S60 Cross Country","XC40","PV444 \/ PV544","P1800","C40"],"123":["Corda","Estina","Tingo"],"124":["353","1.3"],"125":["GT","Roadster"],"126":["Pickup X3","SR-V X3","SUV X3"],"127":["Admiral","GrandTiger","Landmark"],"128":["1111 \u041e\u043a\u0430","2110","2102","2103","2104","2105","2106","2107","2108","2109","21099","2111","2112","2113 Samara","2114 Samara","2115 Samara","2120 \u041d\u0430\u0434\u0435\u0436\u0434\u0430","2123","2129","2328","2329","4x4 (\u041d\u0438\u0432\u0430)","Granta","Kalina","Largus","Priora","Vesta","XRAY","Vesta Cross","2101","XRAY Cross","Largus Cross","Revolution","El Lada","2302 \u0411\u0438\u0437\u043e\u043d","2121 (4x4) Urban","2131 (4x4) Urban","Niva Travel","Niva","Niva Off-road","2121 (4x4) Bronto","Niva Legend","2121 (4x4) \u0424\u043e\u0440\u0430","2121 (4x4) \u0420\u044b\u0441\u044c","Niva Legend Bronto","Granta Cross","1706 \u0427\u0435\u043b\u043d\u043e\u043a","Kalina Cross","2131 (4x4) \u0420\u044b\u0441\u044c"],"129":["1705","1706","2345","2346","2347","2349","2950"],"130":["12 \u0417\u0418\u041c","13 \u0427\u0430\u0439\u043a\u0430","14 \u0427\u0430\u0439\u043a\u0430","\u041c-20 \u041f\u043e\u0431\u0435\u0434\u0430","21 \u0412\u043e\u043b\u0433\u0430","22 \u0412\u043e\u043b\u0433\u0430","24 \u0412\u043e\u043b\u0433\u0430","310221 \u0412\u043e\u043b\u0433\u0430","31029 \u0412\u043e\u043b\u0433\u0430","3102 \u0412\u043e\u043b\u0433\u0430","31105 \u0412\u043e\u043b\u0433\u0430","3110 \u0412\u043e\u043b\u0433\u0430","3111 \u0412\u043e\u043b\u0433\u0430","69","M-1","Volga Siber","\u0413\u0410\u0417\u0435\u043b\u044c","\u0413\u0410\u0417\u0435\u043b\u044c 2705","\u0413\u0410\u0417\u0435\u043b\u044c 3221","\u0413\u0410\u0417\u0435\u043b\u044c 3302","\u0413\u0410\u0417\u0435\u043b\u044c 33023","\u0413\u0410\u0417\u0435\u043b\u044c Next","\u0421\u043e\u0431\u043e\u043b\u044c","\u0421\u043e\u0431\u043e\u043b\u044c 2217","\u0421\u043e\u0431\u043e\u043b\u044c 2310","\u0421\u043e\u0431\u043e\u043b\u044c 2752","\u0413\u0410\u0417\u0435\u043b\u044c 2747","2330 \u0422\u0438\u0433\u0440","67","64","\u0410","\u041c-72","23 \u0412\u043e\u043b\u0433\u0430","3105 \u0412\u043e\u043b\u0433\u0430","2308 \u0410\u0442\u0430\u043c\u0430\u043d","\u0413\u0410\u0417\u0435\u043b\u044c NN"],"131":["1102 \u0422\u0430\u0432\u0440\u0438\u044f","1103 \u0421\u043b\u0430\u0432\u0443\u0442\u0430","1105 \u0414\u0430\u043d\u0430","965 \u0417\u0430\u043f\u043e\u0440\u043e\u0436\u0435\u0446","966 \u0417\u0430\u043f\u043e\u0440\u043e\u0436\u0435\u0446","968 \u0417\u0430\u043f\u043e\u0440\u043e\u0436\u0435\u0446","Chance","Forza","Sens","Vida","11055","Lanos"],"132":["110","111","114","117","4104","4105"],"133":["2125","2126","2715","2717","21261","\u041c\u043e\u0441\u043a\u0432\u0438\u0447-412"],"134":["967","969","1302"],"135":["2136","2137","2138","2140","2141","2335","2733","2734","400","410","420","430","407","408","411","412","422","432","424","426","427","433","434","\u0414\u0443\u044d\u0442","\u0418\u0432\u0430\u043d \u041a\u0430\u043b\u0438\u0442\u0430","\u041a\u043d\u044f\u0437\u044c \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440","\u0421\u0432\u044f\u0442\u043e\u0433\u043e\u0440","\u042e\u0440\u0438\u0439 \u0414\u043e\u043b\u0433\u043e\u0440\u0443\u043a\u0438\u0439","401","402","403","423","3","3e"],"136":["2203","977"],"137":["Aquila","C10","C190","Hyundai Accent","Hyundai Santa Fe Classic","Hyundai Sonata","Road Partner","Tager","Vega","Vortex Corda","Vortex Estina","Vortex Tingo","\u042130","Hardy","Master (LC100)"],"138":["2206","3151","31512","31514","31519","3153","3159","3160","452 \u0411\u0443\u0445\u0430\u043d\u043a\u0430","469","Hunter","Patriot","Pickup","\u041a\u0430\u0440\u0433\u043e","\u0421\u0438\u043c\u0431\u0438\u0440","3303","3741","3909","\u041f\u0440\u043e\u0444\u0438","3962","39094","39095","2360","29891","450"],"139":["Gentra","Matiz","Nexia","R2","R4"],"140":["WAY M1","WAY M2","WAY V1","GS8","Aion S","Aion LX","Aion Y","GN8","GS5","Aion V","GE3"],"141":["T600","Z300","SR9","X7","Coupa"],"142":["Tunland","Gratour","Sauvana","Toano","View CS2","Alpha Van"],"143":["Agera","CC8S","CCR","CCX","One:1","Regera"],"144":["540C","570GT","570S","650S","675LT","F1","MP4-12C","P1","720S","Senna","GT","600LT","Artura"],"145":["G80","G90","G70","GV80","GV70","GV60"],"146":["\u0421-3\u0410","\u0421-3\u0414","\u0421-1\u041b"],"147":["Qute"],"148":["G-modell","Pinzgauer"],"149":["Megabusa","SEiGHT","SEi & Sport"],"150":["MK2"],"151":["DS 3","DS 4","DS 4 Crossback","DS 5","DS 7 Crossback","DS 3 Crossback"],"152":["H3","H5"],"517":["\u041006","\u041007","11"],"518":["UFO"],"519":["57","T603","T613","T700"],"520":["2110","2111","2310","2312"],"521":["Spitfire","TR3"],"522":["Rekord"],"523":["B1000"],"524":["DMC-12"],"525":["MB","CJ","Jeepster"],"526":["Ideal"],"527":["762"],"528":["A01"],"529":["Sherpa"],"530":["3=6"],"531":["2160"],"532":["TX1","TX4","TXII"],"533":["HMMWV (Humvee)"],"534":["Mini","FX4","Montego"],"535":["522"],"536":["Florida"],"537":["QM5","SM3 Z.E","SM5","SM6","QM3","QM6","SM3"],"538":["21541 (\u0421\u0442\u0430\u043b\u043a\u0435\u0440)"],"539":["110","101"],"547":["378 GT Zagato","Ace","Aceca","Cobra"],"560":["TXL"],"568":["Diplomat","Trumpf Junior"],"569":["A610","GTA","A110","A310"],"570":["Eagle","Hornet"],"571":["Atom"],"572":["Speedster"],"573":["Senat","Komendant"],"574":["100","3000"],"575":["A112"],"576":["EU260","Luba (XB624)","A1","BJ212","BJ2020","EU5","BJ40S","EU7"],"577":["BD-1322"],"578":["E200","E300","E100"],"579":["Freeclimber"],"580":["Vintage"],"581":["evA-4"],"582":["Type 3","CD"],"583":["2000","Hansa 1100"],"584":["Fighter","Blenheim","Blenheim Speedster"],"585":["C12"],"586":["V16T"],"587":["T-Rex"],"588":["L-29"],"589":["Bigua","Guara","Mangusta","Pantera","Vallelunga"],"590":["D6"],"591":["Firedome","Fireflite","Custom"],"592":["D8","D8 GTO"],"593":["GD04B"],"594":["SS"],"595":["Series V","Series IV"],"596":["TXL","VX","LX"],"597":["Karma"],"598":["132p","Polonez","125p","126p","127p"],"599":["6500 Land King"],"600":["MPV"],"601":["Troy"],"602":["Roadster"],"603":["Madison"],"604":["97","610"],"605":["Polarsun"],"606":["Kabine"],"607":["Ambassador","Contessa"],"608":["K6"],"609":["853","830"],"610":["ClubSport R8"],"611":["Deluxe Eight"],"612":["LeBaron"],"613":["Elba","Mille","Mini"],"614":["S1"],"615":["Imperator 108i","Spyder"],"616":["Interceptor","S-V8"],"617":["X-Bow"],"618":["JS 51"],"619":["GTS","LM 400","LM 500","Marcasite"],"620":["5EXi","Sportster"],"621":["Alto","800","1000","Wagon R","Zen","Esteem","Versa","Baleno","Gypsy","Omni"],"622":["Monte Carlo","Track","Club"],"623":["M.Go","M8","MC","Virgo","F8C"],"624":["TF 1800"],"625":["Ambassador"],"626":["ES6","ES8","ET7","E\u04216","ET5"],"627":["2500 GT"],"628":["200\/250","Clipper","Custom Eight","One-Twenty","Twelve","Twin Six"],"629":["Esperante","Roadster"],"630":["Cevennes","Hemera","Speedster II"],"631":["Porter"],"632":["118NE","Padmini"],"633":["GTB","GTE"],"634":["3","5"],"635":["Mangusta"],"636":["1500"],"637":["Robin","Scimitar"],"638":["Tropica Roadster"],"639":["Beast","Tank"],"640":["C_Two","Concept_One"],"641":["TV41"],"642":["Saina","Tiba"],"643":["PS10"],"644":["1300\/1500","1307","Vedette"],"645":["50","120"],"646":["Golden Hawk","President 8"],"647":["Zero"],"648":["City"],"649":["Tramontana"],"650":["Tamora","450","350","420","Cerbera","Taimar","Tuscan","S-Series","400","Griffith","Sagaris","390","Tasmin","280","Chimaera"],"651":["GTR"],"652":["Viva","Astra","Cavalier"],"653":["W8","M12"],"654":["400 GT","210","260","300 Atlantique"],"655":["Fenyr SuperSport","Lykan HyperSport"],"656":["W40","W24"],"657":["EX5","W6"],"658":["G3","P7","P5"],"659":["E10"],"660":["ST1"],"661":["2317"],"662":["\u042298"],"663":["\u0421-24"],"665":["V","U"],"666":["E-HS3","E-HS9","E-QM5","H5","HS5","HS7","H9","H7","HQ9"],"667":["Free","Dreamer","Dream"],"671":["E20X"],"672":["Star Asta","Zhengtu (Fighting)"],"673":["Asena 224M"],"677":["ET5"],"675":["One","L9","L7"],"676":["001","009"],"678":["\u04215","C5"],"682":["X","X EV"],"683":["M5","M7"],"687":["SF5"],"688":["01","06","09"],"690":["Ateca","Born","Formentor","Leon"],"691":["300","500"],"693":["Alpha-T","Alpha-S"],"694":["i-PRO","i-VAN","i-JET","i-JOY"],"697":["Type A"],"699":["E5","X3","X3 pro"],"700":["T03","C11"],"701":["3","1","2"],"703":["11"],"704":["X70 Plus","X95"],"706":["Air"],"708":["R1T","R1S"],"709":["Maxus EV30"],"710":["Atlant","Argo"],"711":["Marvel R","iMAX 8","i5"],"712":["X","Z"],"716":["770"],"717":["Aito M5","Aito M7"],"718":["SD"],"781":["VS5","VS7","VA3"],"788":["Z6"]}
	}),
	components: {
		KiaSelect,
	},
}
</script>