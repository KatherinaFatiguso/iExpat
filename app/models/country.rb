class Country < ActiveRecord::Base
  has_many :country_languages # (this is the join table, must be included) 
  has_many :languages, through: :country_languages

  has_many :country_industries # (this is the join table, must be included) 
  has_many :industries, through: :country_industries
end
