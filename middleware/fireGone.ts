import { Middleware } from '@nuxt/types'

const fireGone: Middleware = ({ route, error }) => {
  const pagesGone = [
    '/contacts',
    '/flow',
    '/guide',
    '/print/flow',
    '/cards/details-of-confirmed-cases',
    '/cards/number-of-confirmed-cases',
    '/cards/attributes-of-confirmed-cases',
    '/cards/number-of-tested',
    '/cards/number-of-reports-to-health-consultation-desk',
    '/cards/number-of-reports-to-health-center-desk'
  ]

  if (pagesGone.some(page => route.path.includes(page))) {
    error({ statusCode: 410 })
  }
}

export default fireGone
