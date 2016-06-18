class ChangeColumnDefault < ActiveRecord::Migration
  def change
    change_column :users, :children, :integer, default: 0
  end
end
