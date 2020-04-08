<template>
  <div :class="$style.container">
    <p :class="$style.heading">
      <span :class="[$style.icon, $style.top]">
        <SentimentIcon aria-hidden="true" />
      </span>
      <span :class="$style.fzMedium">{{ $t('不安に思う方') }}</span>
    </p>

    <ul :class="[$style.rectContainer, $style.triple]">
      <li :class="$style.symptom">
        {{ $t('微熱') }}
      </li>
      <li :class="$style.symptom">
        {{ $t('軽い咳') }}
      </li>
      <li :class="$style.symptom">
        {{ $t('感染の不安') }}
      </li>
    </ul>
    <a
      v-scroll-to="{
        el: '#consult',
        onDone: onDoneScroll
      }"
      href="#consult"
      :class="[$style.button, $style.clickable]"
    >
      <span :class="$style.text">{{ $t('新型コロナ専用健康相談窓口へ') }}</span>
      <ArrowForwardIcon :class="$style.icon" />
    </a>
  </div>
</template>

<script lang="ts">
import { onDoneScroll } from '@/utils/vueScrollTo'
import ArrowForwardIcon from '@/static/flow/responsive/arrow_forward.svg'
import SentimentIcon from '@/static/flow/responsive/sentiment_very_dissatisfied.svg'

export default {
  components: { ArrowForwardIcon, SentimentIcon },
  methods: { onDoneScroll }
}
</script>

<style module lang="scss">
@import '@/components/flow/flow_sp.scss';

.rectContainer {
  // suspect
  &.triple {
    margin-left: px2vw(-11);
    margin-right: px2vw(-11);

    > .symptom {
      margin-left: px2vw(11);
      margin-right: px2vw(11);
      flex-grow: 10;
    }
  }
}
// suspect
.callcenter {
  margin-top: px2vw(25);
  text-align: center;

  .open {
    margin-top: px2vw(10);
  }
}

@include largerThan($small) {
  $vw: 960;

  .rectContainer {
    &.triple {
      margin-left: px2vw(-11, $vw);
      margin-right: px2vw(-11, $vw);

      > .symptom {
        margin-left: px2vw(11, $vw);
        margin-right: px2vw(11, $vw);
      }
    }
  }
  // suspect
  .callcenter {
    margin-top: px2vw(25, $vw);

    .open {
      margin-top: px2vw(10, $vw);
    }
  }
}
</style>
