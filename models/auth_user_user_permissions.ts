import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { auth_permission, auth_permissionId } from './auth_permission';
import type { auth_user, auth_userId } from './auth_user';

export interface auth_user_user_permissionsAttributes {
  id: number;
  user_id: number;
  permission_id: number;
}

export type auth_user_user_permissionsPk = "id";
export type auth_user_user_permissionsId = auth_user_user_permissions[auth_user_user_permissionsPk];
export type auth_user_user_permissionsOptionalAttributes = "id";
export type auth_user_user_permissionsCreationAttributes = Optional<auth_user_user_permissionsAttributes, auth_user_user_permissionsOptionalAttributes>;

export class auth_user_user_permissions extends Model<auth_user_user_permissionsAttributes, auth_user_user_permissionsCreationAttributes> implements auth_user_user_permissionsAttributes {
  id!: number;
  user_id!: number;
  permission_id!: number;

  // auth_user_user_permissions belongsTo auth_permission via permission_id
  permission!: auth_permission;
  getPermission!: Sequelize.BelongsToGetAssociationMixin<auth_permission>;
  setPermission!: Sequelize.BelongsToSetAssociationMixin<auth_permission, auth_permissionId>;
  createPermission!: Sequelize.BelongsToCreateAssociationMixin<auth_permission>;
  // auth_user_user_permissions belongsTo auth_user via user_id
  user!: auth_user;
  getUser!: Sequelize.BelongsToGetAssociationMixin<auth_user>;
  setUser!: Sequelize.BelongsToSetAssociationMixin<auth_user, auth_userId>;
  createUser!: Sequelize.BelongsToCreateAssociationMixin<auth_user>;

  static initModel(sequelize: Sequelize.Sequelize): typeof auth_user_user_permissions {
    return auth_user_user_permissions.init({
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
    tableName: 'auth_user_user_permissions',
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
        name: "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "user_id" },
          { name: "permission_id" },
        ]
      },
      {
        name: "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm",
        using: "BTREE",
        fields: [
          { name: "permission_id" },
        ]
      },
    ]
  });
  }
}
