import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { auth_group, auth_groupId } from './auth_group';
import type { auth_permission, auth_permissionId } from './auth_permission';

export interface auth_group_permissionsAttributes {
  id: number;
  group_id: number;
  permission_id: number;
}

export type auth_group_permissionsPk = "id";
export type auth_group_permissionsId = auth_group_permissions[auth_group_permissionsPk];
export type auth_group_permissionsOptionalAttributes = "id";
export type auth_group_permissionsCreationAttributes = Optional<auth_group_permissionsAttributes, auth_group_permissionsOptionalAttributes>;

export class auth_group_permissions extends Model<auth_group_permissionsAttributes, auth_group_permissionsCreationAttributes> implements auth_group_permissionsAttributes {
  id!: number;
  group_id!: number;
  permission_id!: number;

  // auth_group_permissions belongsTo auth_group via group_id
  group!: auth_group;
  getGroup!: Sequelize.BelongsToGetAssociationMixin<auth_group>;
  setGroup!: Sequelize.BelongsToSetAssociationMixin<auth_group, auth_groupId>;
  createGroup!: Sequelize.BelongsToCreateAssociationMixin<auth_group>;
  // auth_group_permissions belongsTo auth_permission via permission_id
  permission!: auth_permission;
  getPermission!: Sequelize.BelongsToGetAssociationMixin<auth_permission>;
  setPermission!: Sequelize.BelongsToSetAssociationMixin<auth_permission, auth_permissionId>;
  createPermission!: Sequelize.BelongsToCreateAssociationMixin<auth_permission>;

  static initModel(sequelize: Sequelize.Sequelize): typeof auth_group_permissions {
    return auth_group_permissions.init({
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    group_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'auth_group',
        key: 'id'
      }
    },
    permission_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'auth_permission',
        key: 'id'
      }
    }
  }, {
    sequelize,
    tableName: 'auth_group_permissions',
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
        name: "auth_group_permissions_group_id_permission_id_0cd325b0_uniq",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "group_id" },
          { name: "permission_id" },
        ]
      },
      {
        name: "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm",
        using: "BTREE",
        fields: [
          { name: "permission_id" },
        ]
      },
    ]
  });
  }
}
