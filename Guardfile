require 'guard/compat/plugin'

module ::Guard
  class ProfileRender < ::Guard::Plugin
    def run_on_modifications(paths)
      `python render.py`
    end
  end
end

guard 'ProfileRender' do
  watch('profile.yml')
  watch('template.html')
end

guard 'livereload' do
  watch(%r{.+\.html$})
  watch(%r{js/.+\.js})
  watch(%r{css/.+\.css})
  watch(%r{img/.+\.(jpg|png)})
end
