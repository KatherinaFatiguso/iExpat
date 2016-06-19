class CountrySkill < ActiveRecord::Base
  belongs_to :country
  belongs_to :industry
end
