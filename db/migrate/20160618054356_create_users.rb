class CreateUsers < ActiveRecord::Migration
  def change
    create_table :users do |t|
      t.string :name
      t.string :passport_country
      t.date :dob
      t.string :gender
      t.string :marital
      t.integer :children, default: 0

      t.timestamps null: false
    end
  end
end
