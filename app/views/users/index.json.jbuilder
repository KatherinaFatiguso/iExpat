json.array!(@users) do |user|
  json.extract! user, :id, :name, :passport_country, :dob, :gender, :marital, :children
  json.url user_url(user, format: :json)
end
