class User < ActiveRecord::Base
  has_many :user_languages # (this is the join table, must be included) 
  has_many :languages, through: :user_languages
end
