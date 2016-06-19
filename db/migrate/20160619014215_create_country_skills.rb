class CreateCountrySkills < ActiveRecord::Migration
  def change
    create_table :country_skills do |t|
      t.references :country, index: true, foreign_key: true
      t.references :industry, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
