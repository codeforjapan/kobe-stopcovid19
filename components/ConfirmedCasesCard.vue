<template>
  <data-view :title="title" :title-id="titleId" :date="date" :url="url">
    <template v-slot:button>
      <ul :class="$style.note">
        <li>
          {{ $t('注）神戸市外在住者は含まれていない') }}
        </li>
        <li>
          {{ $t('注）「検査件数総数」には、検査中のものを含みます。') }}
        </li>
        <li>
          {{
            $t(
              '注）「治癒確認（退院等）」とは検査で病原体を保有していないことが確認できた人 ( 他疾患で入院中の人を含む )。'
            )
          }}
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
