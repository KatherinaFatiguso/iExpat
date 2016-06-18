class Language < ActiveRecord::Base
  has_many :user_languages # (this is the join table, must be included)   
  has_many :users, through: :user_languages
end
