import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { auth_group_permissions, auth_group_permissionsId } from './auth_group_permissions';
import type { auth_user_groups, auth_user_groupsId } from './auth_user_groups';

export interface auth_groupAttributes {
  id: number;
  name: string;
}

export type auth_groupPk = "id";
export type auth_groupId = auth_group[auth_groupPk];
export type auth_groupOptionalAttributes = "id";
export type auth_groupCreationAttributes = Optional<auth_groupAttributes, auth_groupOptionalAttributes>;

export class auth_group extends Model<auth_groupAttributes, auth_groupCreationAttributes> implements auth_groupAttributes {
  id!: number;
  name!: string;

  // auth_group hasMany auth_group_permissions via group_id
  auth_group_permissions!: auth_group_permissions[];
  getAuth_group_permissions!: Sequelize.HasManyGetAssociationsMixin<auth_group_permissions>;
  setAuth_group_permissions!: Sequelize.HasManySetAssociationsMixin<auth_group_permissions, auth_group_permissionsId>;
  addAuth_group_permission!: Sequelize.HasManyAddAssociationMixin<auth_group_permissions, auth_group_permissionsId>;
  addAuth_group_permissions!: Sequelize.HasManyAddAssociationsMixin<auth_group_permissions, auth_group_permissionsId>;
  createAuth_group_permission!: Sequelize.HasManyCreateAssociationMixin<auth_group_permissions>;
  removeAuth_group_permission!: Sequelize.HasManyRemoveAssociationMixin<auth_group_permissions, auth_group_permissionsId>;
  removeAuth_group_permissions!: Sequelize.HasManyRemoveAssociationsMixin<auth_group_permissions, auth_group_permissionsId>;
  hasAuth_group_permission!: Sequelize.HasManyHasAssociationMixin<auth_group_permissions, auth_group_permissionsId>;
  hasAuth_group_permissions!: Sequelize.HasManyHasAssociationsMixin<auth_group_permissions, auth_group_permissionsId>;
  countAuth_group_permissions!: Sequelize.HasManyCountAssociationsMixin;
  // auth_group hasMany auth_user_groups via group_id
  auth_user_groups!: auth_user_groups[];
  getAuth_user_groups!: Sequelize.HasManyGetAssociationsMixin<auth_user_groups>;
  setAuth_user_groups!: Sequelize.HasManySetAssociationsMixin<auth_user_groups, auth_user_groupsId>;
  addAuth_user_group!: Sequelize.HasManyAddAssociationMixin<auth_user_groups, auth_user_groupsId>;
  addAuth_user_groups!: Sequelize.HasManyAddAssociationsMixin<auth_user_groups, auth_user_groupsId>;
  createAuth_user_group!: Sequelize.HasManyCreateAssociationMixin<auth_user_groups>;
  removeAuth_user_group!: Sequelize.HasManyRemoveAssociationMixin<auth_user_groups, auth_user_groupsId>;
  removeAuth_user_groups!: Sequelize.HasManyRemoveAssociationsMixin<auth_user_groups, auth_user_groupsId>;
  hasAuth_user_group!: Sequelize.HasManyHasAssociationMixin<auth_user_groups, auth_user_groupsId>;
  hasAuth_user_groups!: Sequelize.HasManyHasAssociationsMixin<auth_user_groups, auth_user_groupsId>;
  countAuth_user_groups!: Sequelize.HasManyCountAssociationsMixin;

  static initModel(sequelize: Sequelize.Sequelize): typeof auth_group {
    return auth_group.init({
    id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    name: {
      type: DataTypes.STRING(150),
      allowNull: false,
      unique: "name"
    }
  }, {
    sequelize,
    tableName: 'auth_group',
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
        name: "name",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "name" },
        ]
      },
    ]
  });
  }
}
