class CreateUserIndustries < ActiveRecord::Migration
  def change
    create_table :user_industries do |t|
      t.references :user, index: true, foreign_key: true
      t.references :industry, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
