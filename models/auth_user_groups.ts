import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { auth_group, auth_groupId } from './auth_group';
import type { auth_user, auth_userId } from './auth_user';

export interface auth_user_groupsAttributes {
  id: number;
  user_id: number;
  group_id: number;
}

export type auth_user_groupsPk = "id";
export type auth_user_groupsId = auth_user_groups[auth_user_groupsPk];
export type auth_user_groupsOptionalAttributes = "id";
export type auth_user_groupsCreationAttributes = Optional<auth_user_groupsAttributes, auth_user_groupsOptionalAttributes>;

export class auth_user_groups extends Model<auth_user_groupsAttributes, auth_user_groupsCreationAttributes> implements auth_user_groupsAttributes {
  id!: number;
  user_id!: number;
  group_id!: number;

  // auth_user_groups belongsTo auth_group via group_id
  group!: auth_group;
  getGroup!: Sequelize.BelongsToGetAssociationMixin<auth_group>;
  setGroup!: Sequelize.BelongsToSetAssociationMixin<auth_group, auth_groupId>;
  createGroup!: Sequelize.BelongsToCreateAssociationMixin<auth_group>;
  // auth_user_groups belongsTo auth_user via user_id
  user!: auth_user;
  getUser!: Sequelize.BelongsToGetAssociationMixin<auth_user>;
  setUser!: Sequelize.BelongsToSetAssociationMixin<auth_user, auth_userId>;
  createUser!: Sequelize.BelongsToCreateAssociationMixin<auth_user>;

  static initModel(sequelize: Sequelize.Sequelize): typeof auth_user_groups {
    return auth_user_groups.init({
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    user_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'auth_user',
        key: 'id'
      }
    },
    group_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'auth_group',
        key: 'id'
      }
    }
  }, {
    sequelize,
    tableName: 'auth_user_groups',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "id" },
        ]
      },
      {
        name: "auth_user_groups_user_id_group_id_94350c0c_uniq",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "user_id" },
          { name: "group_id" },
        ]
      },
      {
        name: "auth_user_groups_group_id_97559544_fk_auth_group_id",
        using: "BTREE",
        fields: [
          { name: "group_id" },
        ]
      },
    ]
  });
  }
}
