<template>
	<view v-if="show" class="uni-noticebar" :style="{backgroundColor:backgroundColor,color:color}" @click="onClick">
		<view v-if="showClose === 'true' || showClose === true" class="uni-noticebar__close">
			<uni-icon type="closefill" size="12"></uni-icon>
		</view>
		<view class="uni-noticebar__content" :class="setContenClass">
			<view v-if="showIcon === 'true' || showIcon === true" class="uni-noticebar__content-icon" :style="{backgroundColor:backgroundColor,color:color}">
				<uni-icon type="sound" size="14" :color="color"></uni-icon>
			</view>
			<view class="uni-noticebar__content-text" :class="setTextClass">
				<!-- #ifdef H5 -->
				<view class="uni-noticebar__content-inner" :id="elId" :style="{'animation-duration': animation,'-webkit-animation-duration': animation}">{{text}}</view>
				<!-- #endif -->
				<!-- #ifndef H5 -->
				<view class="uni-noticebar__content-inner" :id="elId" :style="{'animation': animation,'-webkit-animation': animation}">{{text}}</view>
				<!-- #endif -->
			</view>
			<view class="uni-noticebar__content-more" v-if="showGetMore === 'true' || showGetMore === true" @click="clickMore" :style="{width:moreText ? '180upx' : '20px'}">
				<view class="uni-noticebar__content-more-text" v-if="moreText">{{moreText}}</view>
				<uni-icon type="arrowright" size="14"></uni-icon>
			</view>
		</view>
	</view>
</template>

<script>
	import uniIcon from '../uni-icon/uni-icon.vue'
	export default {
		name: "uni-notice-bar",
		components: {
			uniIcon
		},
		props: {
			text: String,
			moreText: String,
			backgroundColor: {
				type: String,
				default: '#fffbe8'
			},
			speed: { //默认1s滚动100px
				type: [String, Number],
				default: 100
			},
			color: {
				type: String,
				default: '#de8c17'
			},
			single: { //是否单行
				type: [String, Boolean],
				default: false
			},
			scrollable: { //是否滚动，添加后控制单行效果取消
				type: [String, Boolean],
				default: false
			},
			showIcon: { //是否显示左侧icon
				type: [String, Boolean],
				default: false
			},
			showGetMore: { //是否显示右侧查看更多
				type: [String, Boolean],
				default: false
			},
			showClose: { //是否显示左侧关闭按钮
				type: [String, Boolean],
				default: false
			}
		},
		data() {
			const elId = `Uni_${Math.ceil(Math.random() * 10e5).toString(36)}`
			return {
				elId: elId,
				show: true,
				animation: ''
			}
		},
		watch: {
			text(newValue, oldValue) {
				this.$nextTick(() => {
					setTimeout(this.setAnimation, 200)
				})
			}
		},
		computed: {
			setTextClass() {
				let classList = []
				if (this.scrollable === true || this.scrollable === 'true') {
					classList.push('uni-noticebar--scrollable')
				} else {
					if (this.single === 'true' || this.single === true || this.moreText) {
						classList.push('uni-noticebar--single')
					}
				}
				return classList
			},
			setContenClass() {
				let classList = []
				if (this.scrollable === true || this.scrollable === 'true' || this.single === 'true' || this.single === true ||
					this.moreText) {
					classList.push('uni-noticebar--flex')
				}
				return classList
			}
		},
		// #ifdef H5
		mounted() { //在h5的时候走mounted，app和小程序走onReady
			this.setAnimation()
		},
		// #endif
		// #ifndef H5
		onReady() {
			this.setAnimation()
		},
		// #endif
		methods: {
			clickMore() {
				this.$emit('getmore')
			},
			onClick(e) {
				let clientX = e.touches ? (e.touches[0] ? e.touches[0].clientX : e.changedTouches[0].clientX) : e.detail.clientX;
				if (uni.upx2px(48) + 12 > clientX && (String(this.showClose) === 'true')) {
					this.show = false
					this.$emit('close')
				}
				this.$emit('click')
			},
			setAnimation() {
				if (this.scrollable === false || this.scrollable === 'false') {
					return;
				}
				//#ifdef MP-TOUTIAO
				setTimeout(() => {
					uni.createSelectorQuery().select(`#${this.elId}`).boundingClientRect().exec((ret) => {
						console.log(ret)
						this.animation = `notice ${ret[0].width / this.speed}s linear infinite both`;
					});
				}, 500)
				// #endif
				//#ifdef H5
				setTimeout(() => {
					uni.createSelectorQuery().select(`#${this.elId}`).boundingClientRect().exec((ret) => {
						this.animation = `${ret[0].width / this.speed}s`;
					});
				}, 200)
				// #endif
				// #ifndef MP-TOUTIAO || H5
				uni.createSelectorQuery().select(`#${this.elId}`).boundingClientRect().exec((ret) => {
					this.animation = `notice ${ret[0].width / this.speed}s linear infinite both`;
				});
				// #endif
			}
		}
	}
</script>

<style>
	@charset "UTF-8";

	.uni-noticebar {
		padding: 12upx 24upx;
		font-size: 24upx;
		line-height: 1.5;
		margin: 10upx 0;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		justify-content: left
	}

	.uni-noticebar__close {
		color: #999;
		margin-right: 24upx;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center
	}

	.uni-noticebar__content {
		flex: 1;
		overflow: hidden
	}

	.uni-noticebar__content.uni-noticebar--flex {
		flex: 1;
		display: flex;
		flex-direction: row
	}

	.uni-noticebar__content-icon {
		display: inline-block;
		z-index: 1;
		padding-right: 12upx
	}

	.uni-noticebar__content-more {
		width: 180upx;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		justify-content: flex-end;
		word-break: keep-all;
		margin-left: 10upx;
		color: #999
	}

	.uni-noticebar__content-more-text {
		font-size: 24upx;
		white-space: nowrap
	}

	.uni-noticebar__content-text {
		word-break: break-all;
		line-height: 1.5;
		display: inline
	}

	.uni-noticebar__content-text.uni-noticebar--single {
		text-overflow: ellipsis;
		white-space: nowrap;
		overflow: hidden
	}

	.uni-noticebar__content-text.uni-noticebar--scrollable {
		flex: 1;
		display: block;
		overflow: hidden
	}

	.uni-noticebar__content-text.uni-noticebar--scrollable .uni-noticebar__content-inner {
		padding-left: 100%;
		white-space: nowrap;
		display: inline-block;
		/* #ifdef H5 */
		animation-name: notice;
		animation-timing-function: linear;
		animation-fill-mode: both;
		animation-iteration-count: infinite;
		/* #endif */
		transform: translateZ(0)
	}

	.uni-noticebar__content-inner {
		font-size: 24upx;
		display: inline
	}

	@keyframes notice {
		100% {
			transform: translate3d(-100%, 0, 0)
		}
	}
</style>