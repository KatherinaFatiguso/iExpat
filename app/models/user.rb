class User < ActiveRecord::Base
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable
  has_many :user_languages # (this is the join table, must be included) 
  has_many :languages, through: :user_languages

  has_many :user_industries # (this is the join table, must be included) 
  has_many :industries, through: :user_industries

end
