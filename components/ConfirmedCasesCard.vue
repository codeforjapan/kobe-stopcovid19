<template>
  <data-view :title="title" :title-id="titleId" :date="date" :url="url">
    <template v-slot:button>
      <ul :class="$style.note">
        <li>
          {{ $t('（注）市外で感染が発覚した人は含まれていない') }}
        </li>
      </ul>
    </template>
    <slot />
  </data-view>
</template>

<style lang="scss" module>
.note {
  margin-top: 10px;
  margin-bottom: 0;
  padding-left: 0 !important;
  font-size: 12px;
  color: $gray-3;

  > li {
    list-style-type: none;
  }
}
</style>

<script lang="ts">
import Vue from 'vue'
import DataView from '@/components/DataView.vue'

export default Vue.extend({
  components: { DataView },
  props: {
    title: {
      type: String,
      default: ''
    },
    titleId: {
      type: String,
      default: ''
    },
    date: {
      type: String,
      default: ''
    },
    url: {
      type: String,
      default: ''
    }
  }
})
</script>
