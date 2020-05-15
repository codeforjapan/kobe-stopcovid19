<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-view
      :title="$t('検査陽性者の状況')"
      :title-id="'details-of-confirmed-cases'"
      :date="Data.patients.date"
    >
      <template v-slot:button>
        <ul :class="$style.note">
          <li>
            {{ $t('注）神戸市外在住者は含まれていない') }}
          </li>
          <li>
            {{
              $t(
                '注）「治癒確認（退院等）」とは検査で病原体を保有していないことが確認できた人 ( 他疾患で入院中の人を含む )。'
              )
            }}
          </li>
          <li>
            {{ $t('注）「入院・入居中」は、宿泊療養に移行した人を含みます。') }}
          </li>
        </ul>
      </template>
      <confirmed-cases-details-table
        :aria-label="$t('検査陽性者の状況')"
        v-bind="confirmedCases"
      />
      <template v-slot:footer>
        <open-data-link
          :url="'https://data.city.kobe.lg.jp/data/dataset/32576-7-5-0-4'"
        />
      </template>
    </data-view>
  </v-col>
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

<script>
import Data from '@/data/data.json'
import formatConfirmedCases from '@/utils/formatConfirmedCases'
import DataView from '@/components/DataView.vue'
import ConfirmedCasesDetailsTable from '@/components/ConfirmedCasesDetailsTable.vue'
import OpenDataLink from '@/components/OpenDataLink'

export default {
  components: {
    DataView,
    ConfirmedCasesDetailsTable,
    OpenDataLink
  },
  data() {
    // 検査陽性者の状況
    const confirmedCases = formatConfirmedCases(Data.main_summary)

    const data = {
      Data,
      confirmedCases
    }
    return data
  }
}
</script>
