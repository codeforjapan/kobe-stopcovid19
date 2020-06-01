<template>
  <div class="Error">
    <suspended />
    <div class="Error-BodyContainer">
      <template v-if="isGone">
        <p>
          {{
            $t(
              'このページは神戸市公式ホームページに内容を移動したため、今後更新されません。'
            )
          }}
        </p>
        <p>
          {{
            $t(
              'ブックマークの登録やグラフの埋め込み等をしている場合は、神戸市公式ホームページをご利用いただきますようお願いいたします。'
            )
          }}
        </p>
      </template>
      <template v-else>
        <p>
          {{ $t('アクセスしようとしたページが見つかりませんでした。') }}
        </p>
        <p>
          {{
            $t(
              'ページが移動または削除されたか、URLの入力間違いの可能性があります。'
            )
          }}
        </p>
      </template>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Suspended from '@/components/Suspended.vue'

export default Vue.extend({
  components: {
    Suspended
  },
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  computed: {
    isGone(): boolean {
      return this.error.statusCode === 410
    }
  }
})
</script>

<style lang="scss" scoped>
.Error {
  &-BodyContainer {
    margin-top: 12px;
    padding: 20px;

    @include card-container();

    > p {
      margin-bottom: 0;
      @include body-text();
    }
  }
}
</style>
