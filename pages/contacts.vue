<template>
  <div class="Contacts">
    <page-header class="mb-3">
      {{ $t('お問い合わせ先一覧') }}
    </page-header>
    <StaticCard>
      <h3>
        {{ $t('神戸市電話相談窓口（24時間受付: 多言語対応可）') }}
      </h3>
      <table class="Contacts-CityContactsTable" v-bind="tableAttrs">
        <thead>
          <tr>
            <th class="text-center" scope="col">
              {{ $t('名称・電話番号') }}
            </th>
            <th class="text-center" scope="col">{{ $t('対象者') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              <dl>
                <dt class="Name">
                  {{ $t('新型コロナウィルス専用健康相談窓口') }}
                </dt>
                <dd class="Tel">
                  <a href="tel:0783226250">078-322-6250</a>
                </dd>
              </dl>
            </td>
            <td class="Content">
              {{
                $t(
                  '予防に関すること、感染症・健康不安に対する一般的な相談のある方'
                )
              }}
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              <dl>
                <dt class="Name">{{ $t('帰国者・接触者相談センター') }}</dt>
                <dd class="Tel"><a href="tel:0783226829">078-322-6829</a></dd>
              </dl>
              <p class="Notes">
                {{
                  $t(
                    'お電話がつながりにくい場合は、上記専用健康相談窓口におかけください。'
                  )
                }}
              </p>
            </td>
            <td class="Content">
              <ul>
                <li>{{ $t('感染者との接触があった方') }}</li>
                <li>{{ $t('湖北省等に渡航歴等のある方 ') }}</li>
                <li>
                  {{ $t('風邪の症状や37.5℃以上の発熱が4日以上続いている方') }}
                </li>
              </ul>
              {{ $t('など') }}
              <strong>{{ $t('（下記の相談対象者参照）') }}</strong>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              <dl>
                <dt class="Name">{{ $t('ファクシミリ') }}</dt>
                <dd class="Tel"><a href="tel:0783915532">078-391-5532</a></dd>
              </dl>
              <p class="Notes">
                {{ $t('送付票はこちら:') }}
                <a
                  href="https://www.city.kobe.lg.jp/documents/31680/20200318souhuhyou.pdf"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {{ $t('送付票') }}
                </a>
              </p>
            </td>
            <td class="Content">
              {{ $t('上記相談窓口、相談センター共通で受付しています。') }}
            </td>
          </tr>
        </tbody>
      </table>
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
  created() {
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
      title: this.$t('お問い合わせ先一覧') as string
    }
  }
})
</script>

<style lang="scss">
.Contacts {
  &-CityContactsTable,
  &-SubjectDetailsTable,
  &-WardsContactsTable {
    width: 100%;
    border-collapse: collapse;

    th {
      font-size: 14px !important;
    }

    td {
      padding: 0 16px;
      font-size: 14px;
    }

    @include largerThan($medium) {
      thead tr {
        height: 48px;
      }

      tbody tr {
        height: 96px;
      }

      th,
      tr:not(:last-child) {
        border-top: none;
        border-left: none;
        border-right: none;
        border-bottom: thin solid rgba(0, 0, 0, 0.12);
      }

      tr:last-child {
        border: none;
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

        tr:not(:last-child) {
          border-bottom: thin solid rgba(0, 0, 0, 0.12);
        }
      }

      td {
        display: block;
      }
    }
  }

  &-CityContactsTable .RowHeader {
    .Tel {
      margin-top: 0;
      margin-left: 0;
      font-weight: bold;
    }
    @include lessThan($medium) {
      .Notes {
        font-weight: normal;
      }
    }
  }
}
</style>
