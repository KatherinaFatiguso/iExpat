# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

user = User.create!(email: 'demo@iexpat.com', password: '12345678')
user1 = User.create!(email: 'demo1@iexpat.com', password: '12345678')
user2 = User.create!(email: 'demo2@iexpat.com', password: '12345678')
