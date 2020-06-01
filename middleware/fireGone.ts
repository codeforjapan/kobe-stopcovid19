import { Middleware } from '@nuxt/types'

const fireGone: Middleware = ({ route, error }) => {
  const pagesGone = [
    '/contacts',
    '/flow', // なぜか/flow/ にリダイレクトされるが一応追加しておく
    '/flow/',
    '/guide',
    '/print/flow',
    '/cards/details-of-confirmed-cases',
    '/cards/number-of-confirmed-cases',
    '/cards/attributes-of-confirmed-cases',
    '/cards/number-of-tested',
    '/cards/number-of-reports-to-health-consultation-desk',
    '/cards/number-of-reports-to-health-center-desk'
  ]

  if (pagesGone.includes(route.fullPath)) {
    error({ statusCode: 410 })
  }
}

export default fireGone
