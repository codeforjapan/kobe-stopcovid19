<template>
  <div class="Contacts">
    <page-header class="mb-3">
      {{ $t('神戸市電話相談窓口') }}
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
                  <span> {{ $t('新型コロナウイルス専用健康相談窓口') }} </span>
                  <span> {{ $t('（帰国者・接触者相談センター）') }} </span>
                </dt>
                <dd class="Tel">
                  <a href="tel:0783226250">078-322-6250</a>
                </dd>
              </dl>
            </td>
            <td class="Content">
              <ul>
                <li>
                  {{
                    $t(
                      '予防に関すること、感染症・健康不安に対する一般的な相談のある方'
                    )
                  }}
                </li>
                <li>
                  {{ $t('下記事項のいずれかに該当する方') }}
                  <ol>
                    <li>
                      {{ $t('感染者との接触があり、発熱などの症状のある方') }}
                    </li>
                    <li>
                      {{
                        $t('湖北省等に渡航歴等があり、発熱などの症状のある方 ')
                      }}
                    </li>
                    <li>
                      {{
                        $t('風邪の症状や37.5℃以上の発熱が4日以上続いている方')
                      }}
                    </li>
                  </ol>
                </li>
              </ul>
              {{ $t('（詳細は下記相談対象者参照）') }}
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
                  href="https://www.city.kobe.lg.jp/documents/31680/20200318souhuhyou2.pdf"
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
    <StaticCard>
      <h3>
        {{ $t('相談対象者（帰国者・接触者相談センター）') }}
      </h3>
      <table class="Contacts-SubjectDetailsTable" v-bind="tableAttrs">
        <tbody>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              1. {{ $t('感染者との接触があった方') }}
            </td>
            <td class="Content">
              {{
                $t(
                  '新型コロナウイルス感染症であることが確定した方と濃厚接触歴があり、発熱または呼吸器症状のある方'
                )
              }}
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              2. {{ $t('WHOの公表する流行地域への渡航等があった方') }}
            </td>
            <td class="Content">
              <i18n
                path="37.5度以上の発熱かつ呼吸器症状を有し、発症前14日以内に{pdf}へ渡航または居住していた方、あるいはその地域の居住者との濃厚接触歴がある方"
              >
                <template v-slot:pdf>
                  <a
                    href="https://www.city.kobe.lg.jp/documents/31680/0403ryukochiiki.pdf"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {{ $t('WHOの公表する流行地域（PDF：277KB）') }}
                  </a>
                </template>
              </i18n>
            </td>
          </tr>
          <tr class="MergedLastRow">
            <td class="RowHeader" rowspan="2" v-bind="headingAttrs">
              3. {{ $t('次の相談・受診の目安に当てはまる方') }}
            </td>
            <td class="Content MergedMiddleRow">
              <i18n
                tag="p"
                path="風邪の症状や37.5度以上の発熱が4日以上{elders}続く方"
              >
                <template v-slot:elders>
                  <strong>
                    {{ $t('（高齢者・基礎疾患等※のある方は2日程度）') }}
                  </strong>
                </template>
              </i18n>
              <p>
                {{ $t('注）解熱剤を飲み続けなければならない方も同様です。') }}
              </p>
            </td>
          </tr>
          <tr>
            <td class="Content">
              {{ $t('強いだるさ（倦怠感）や息苦しさ（呼吸困難）がある方') }}
            </td>
          </tr>
        </tbody>
      </table>
      <a
        href="https://www.mhlw.go.jp/content/10900000/000596905.pdf"
        target="_blank"
        rel="noopener noreferrer"
      >
        {{ $t('新型コロナウイルス感染症についての相談・受診の目安') }}
      </a>
      <p>
        {{ $t('※に該当する方は下記の通りです。') }}
      </p>
      <ul>
        <li>{{ $t('高齢者') }}</li>
        <li>
          {{
            $t(
              '糖尿病、心不全、呼吸器疾患（COPD等）の基礎疾患がある方や透析を受けている方'
            )
          }}
        </li>
        <li>{{ $t('免疫抑制剤や抗がん剤等を用いている方') }}</li>
      </ul>
      <p>
        {{
          $t(
            'これらの方々は、重症化しやすいため、この状態が2日程度続く場合には、相談して下さい。'
          )
        }}
      </p>
      <p>
        {{
          $t(
            'なお、妊婦の方も、念のため、重症化しやすい方と同様に、早めの相談をお願いします。'
          )
        }}
      </p>
      <h4>
        {{ $t('お住まいの区および支所の保健センター') }}
      </h4>
      <i18n tag="p" path="{time}の間は、下記でも相談を受け付けています。">
        <template v-slot:time>
          <strong>{{ $t('平日の8時45分から17時15分') }}</strong>
        </template>
      </i18n>
      <table class="Contacts-WardsContactsTable" v-bind="tableAttrs">
        <thead>
          <tr>
            <th class="text-center" scope="col">
              {{ $t('各区および支所') }}
            </th>
            <th class="text-center" scope="col">{{ $t('電話番号') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('東灘区') }}
            </td>
            <td class="Content">
              <a href="tel:0788414131">841-4131</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('灘区') }}
            </td>
            <td class="Content">
              <a href="tel:0788437001">843-7001</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('中央区') }}
            </td>
            <td class="Content">
              <a href="tel:0782324411">232-4411</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('兵庫区') }}
            </td>
            <td class="Content">
              <a href="tel:0785112111">511-2111</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('北区') }}
            </td>
            <td class="Content">
              <a href="tel:0785931111">593-1111</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('北区（北神区役所）') }}
            </td>
            <td class="Content">
              <a href="tel:0789815377">981-5377</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('長田区') }}
            </td>
            <td class="Content">
              <a href="tel:0785792311">579-2311</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('須磨区') }}
            </td>
            <td class="Content">
              <a href="tel:0787314341">731-4341</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('北須磨支所') }}
            </td>
            <td class="Content">
              <a href="tel:0787931335">793-1335</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('垂水区') }}
            </td>
            <td class="Content">
              <a href="tel:0787085151">708-5151</a>
            </td>
          </tr>
          <tr>
            <td class="RowHeader" v-bind="headingAttrs">
              {{ $t('西区') }}
            </td>
            <td class="Content">
              <a href="tel:0789290001">929-0001</a>
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
