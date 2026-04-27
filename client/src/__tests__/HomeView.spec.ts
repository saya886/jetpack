import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'

import HomeView from '../views/HomeView.vue'

describe('HomeView', () => {
  it('renders the initialized project screen', () => {
    const wrapper = mount(HomeView)

    expect(wrapper.text()).toContain('Jetpack')
    expect(wrapper.text()).toContain('Structure only')
  })
})
