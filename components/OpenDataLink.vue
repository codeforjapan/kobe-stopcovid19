<template>
  <a
    v-if="source"
    class="OpenDataLink"
    :href="url"
    target="_blank"
    rel="noopener noreferrer"
  >
    {{ source }}
    <v-icon
      class="ExternalLinkIcon"
      size="15"
      :aria-label="this.$t('別タブで開く')"
      role="img"
      :aria-hidden="false"
    >
      mdi-open-in-new
    </v-icon>
  </a>
  <a
    v-else
    class="OpenDataLink"
    :href="url"
    target="_blank"
    rel="noopener noreferrer"
  >
    {{ $t('オープンデータを入手') }}
    <v-icon
      class="ExternalLinkIcon"
      size="15"
      :aria-label="this.$t('別タブで開く')"
      role="img"
      :aria-hidden="false"
    >
      mdi-open-in-new
    </v-icon>
  </a>
</template>

<style lang="scss">
.OpenDataLink {
  text-decoration: none;
  .ExternalLinkIcon {
    vertical-align: text-bottom;
  }
}
</style>
<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  props: {
    url: {
      type: String,
      default: ''
    },
    source: {
      type: String,
      required: false,
      default: ''
    }
  }
})
</script>
