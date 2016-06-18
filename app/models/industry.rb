class Industry < ActiveRecord::Base
  has_many :user_industries # (this is the join table, must be included) 
  has_many :users, through: :user_industries
end
