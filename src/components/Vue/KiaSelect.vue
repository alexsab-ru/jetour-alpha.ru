<template>
	<div
		class="k-select"
		:class="{'active': isActive, 'selected': isSelected || options.length == 1}"
		@keydown.esc="hide"
		tabindex="-1"
		v-on-click-outside="hide"
	>
		<a
			href="#"
			class="k-select-head"
			@click.prevent="toggle"
		>
			<span class="k-select-label truncate" ref="label">{{options.length == 1 && typeof options[0] != 'object' ? options[0] 
			 : options.length == 1 && typeof options[0] == 'object' ? options[0].name : placeholder}}</span>
			<span class="k-select-arrow flex items-center">
				<svg height="128px" id="Layer_1" style="enable-background:new 0 0 128 128;" version="1.1" viewBox="0 0 128 128" width="128px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><line style="fill:none;stroke-width:14;stroke-linecap:square;stroke-miterlimit:10;" x1="111" x2="64" y1="40.5" y2="87.499"/><line style="fill:none;stroke-width:14;stroke-linecap:square;stroke-miterlimit:10;" x1="64" x2="17" y1="87.499" y2="40.5"/></svg>
			</span>
		</a>
		<transition name="slide">
			<div class="k-select-dropdown" v-show="isActive" v-if="to">
				<a
					href="#"
					v-for="i in 10"
					:key="i"
					:data-val="+i"
					:data-title="ToList(i)"
					v-html="ToList(i)"
					@click.prevent="clickOption"
				></a>
			</div>
			<div class="k-select-dropdown" v-show="isActive" v-else-if="obj">
				<a
					href="#"
					v-for="option in options"
					:key="option.id"
					:data-val="option.id"
					:data-title="option.name"
					:class="{'selected': select === option.id || options.length == 1}"
					@click.prevent="clickOption"
				>{{option.name}}
				</a>
			</div>
			<div class="k-select-dropdown" v-show="isActive" v-else>
				<a
					href="#"
					v-for="(option, idx) in options"
					:key="option"
					:data-val="id ? idx : option"
					:data-title="option"
					:class="{'selected': options.length == 1}"
					@click.prevent="clickOption"
				>{{option}}
				</a>
			</div>
		</transition>
	</div>
</template>

<script>
	import ToListMixin from './to-list'
	import { vOnClickOutside } from '@vueuse/components' //https://vueuse.org/core/onClickOutside/
	export default {
		directives: {
			onClickOutside: vOnClickOutside
		},
		mixins: [ToListMixin],
		props: {
			options: Array,
			placeholder: {
				type: String,
				required: false,
				default: 'Select a Value'
			},
			to: {
				type: Boolean,
				required: false,
				default: false
			},
			id: {
				type: Boolean,
				required: false,
				default: false
			},
			obj: {
				type: Boolean,
				required: false,
				default: false
			},
			select: {
				type: Number && String,
				required: false,
				default: ''
			},
		},
		data: () => ({
			isActive: false,
			isSelected: false,
		}),
		methods: {
			hide() {
				this.isActive = false;
			},
			toggle(e){
				let isBlock =e.currentTarget.parentElement.dataset.block;
				if (isBlock == 'true') {
					return;
				}
				this.isActive = !this.isActive
			},
			clickOption(e){
				const $this = e.currentTarget;
				const $parent = $this.parentElement.parentElement;
				let val = $this.dataset.val;
				let title = $this.dataset.title;
				$parent.querySelectorAll('.k-select-dropdown a').forEach(el=>{
					el.classList.remove('selected')
				})
				$this.classList.add('selected');
				this.$refs.label.innerText = title ? title : val;
				this.isActive = false;
				this.isSelected = true;			
				this.$emit('changed', val)
			},
		},
		mounted(){
			if(this.select != null){
				const opt = this.options.find(item => item.id === this.select);
				if(opt){
					this.$refs.label.innerText = opt.name;
					this.isSelected = true;
				}
			}
		},
		watch: {
			select(n, o){
				// console.log(n, o);
				if(n != null){
					const opt = this.options.find(item => item.id == n);
					this.$refs.label.innerText = opt.name;
					this.isSelected = true;
				}
			}
		},
	}
</script>

<style lang="scss" scoped>
.k-select{
	min-width: 200px;
	display: inline-block;
	position: relative;
	&.selected{
		.k-select-head{
			color: #05141f;
			border-color: #05141f;
			background-color: #fff;
		}
	}
	&.active{
		.k-select-head{
			color: #05141f;
			border-color: #05141f;
			background-color: #fff;
			.k-select-arrow{
				transform: rotate(-180deg);
				svg{
					line{
						stroke: #05141f;
					}
				}
			}
		}
	}
}
.k-select-head{
	height: 40px;
	width: 100%;
	display: inline-flex;
	align-items: center;
	font-weight: normal;
	justify-content: space-between;
	border: 1px solid #CDD0D2;
	padding: 0 10px;
	font-size: 16px;
	color: #697279;
	background-color: transparent;
	transition: all .25s ease;
	@media (max-width: 586px){
		font-size: 14px;
	}
}
.k-select-arrow{
	transform: rotate(0deg);
	transition: all .25s ease;
	svg{
		width: 10px;
		height: auto;
		line{
			stroke: #697279;
			transition: all .25s ease;
		}
	}
}
.k-select-dropdown{
	position: absolute;
	max-height: 200px;
	overflow-y: auto;
	top: 100%;
	left: 0;
	min-width: 100%;
	border: 1px solid #05141f;
	border-top: none;
	background-color: #fff;
	z-index: 100;
	&::-webkit-scrollbar{
		width: 4px;
		background-color: #fff;
	}
	&::-webkit-scrollbar-thumb{
		background-color: #CDD0D2;
	}
	a{
		display: block;
		font-weight: normal;
		text-align: left;
		font-size: 16px;
		padding: 2px 10px;
		transition: all .25s ease;
		background-color: transparent;
		&:hover, &.selected{
			background-color: #f8f8f8;
		}
		@media (max-width: 586px){
			font-size: 14px;
		}
	}
}
</style>