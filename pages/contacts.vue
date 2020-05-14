<template>
  <div class="Contacts">
    <page-header class="mb-3">
      {{ $t('神戸市電話相談窓口') }}
    </page-header>
    <StaticCard>
      <i18n
        path="このページの内容は、神戸市公式ホームページの {link} に移動しました。"
        tag="p"
      >
        <template v-slot:link>
          <a
            href="https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/coronavirus.html#soudansaki"
            target="_blank"
            rel="noopener noreferrer"
          >
            {{ $t('新型コロナウイルスについて') }}
          </a>
        </template>
      </i18n>
    </StaticCard>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
import StaticCard from '@/components/StaticCard.vue'

export default Vue.extend({
  components: {
    PageHeader,
    StaticCard
  },
  data() {
    return {
      pc: true
    }
  },
  computed: {
    tableAttrs(): any {
      return this.pc ? {} : { role: 'presentation' }
    },
    headingAttrs(): any {
      return this.pc ? {} : { role: 'heading', 'aria-level': '3' }
    }
  },
  mounted() {
    if (process.browser) {
      window.addEventListener('resize', this.handleResize)
      this.handleResize()
    }
  },
  destroyed() {
    if (process.browser) {
      window.removeEventListener('resize', this.handleResize)
    }
  },
  methods: {
    handleResize() {
      this.pc = window.innerWidth > 768
    }
  },
  head(): MetaInfo {
    return {
      title: this.$t('神戸市電話相談窓口') as string
    }
  }
})
</script>

<style lang="scss">
.Contacts {
  strong {
    border-bottom: none;
  }

  &-CityContactsTable,
  &-SubjectDetailsTable,
  &-WardsContactsTable {
    width: 100%;
    border-collapse: collapse;

    th {
      font-size: 14px !important;
    }

    td {
      padding: 16px;
      font-size: 14px;
    }

    @include largerThan($medium) {
      thead tr {
        height: 48px;
      }

      tr:last-child,
      .MergedLastRow {
        border: none;
      }

      th,
      tr:not(:last-child):not(.MergedLastRow),
      .MergedMiddleRow {
        border-top: none;
        border-left: none;
        border-right: none;
        border-bottom: thin solid rgba(0, 0, 0, 0.12);
      }
    }

    @include lessThan($medium) {
      thead {
        display: none;
      }

      tbody {
        tr {
          height: auto;

          .RowHeader {
            font-weight: bold;
            border-bottom: none !important;
            padding-top: 12px;
            padding-bottom: 8px;
          }

          .Content {
            padding-bottom: 12px;
          }
        }

        tr:not(:last-child):not(.MergedLastRow) {
          border-bottom: thin solid rgba(0, 0, 0, 0.12);
        }

        .MergedMiddleRow {
          border-bottom: none;
          padding-bottom: 6px !important;
        }
      }

      td {
        display: block;
      }
    }
  }

  &-CityContactsTable,
  &-SubjectDetailsTable {
    @include largerThan($medium) {
      tbody tr {
        height: 96px;
      }
    }
  }

  &-WardsContactsTable {
    @include largerThan($medium) {
      tbody tr {
        height: 2.5em;
      }
    }
  }

  &-CityContactsTable .RowHeader {
    .Tel {
      margin-top: 0;
      margin-left: 0;
      font-weight: bold;
    }

    > span {
      display: block;
    }

    @include lessThan($medium) {
      .Notes {
        font-weight: normal;
      }
    }
  }
}
</style>
