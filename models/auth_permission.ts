import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { auth_group_permissions, auth_group_permissionsId } from './auth_group_permissions';
import type { auth_user_user_permissions, auth_user_user_permissionsId } from './auth_user_user_permissions';
import type { django_content_type, django_content_typeId } from './django_content_type';

export interface auth_permissionAttributes {
  id: number;
  name: string;
  content_type_id: number;
  codename: string;
}

export type auth_permissionPk = "id";
export type auth_permissionId = auth_permission[auth_permissionPk];
export type auth_permissionOptionalAttributes = "id";
export type auth_permissionCreationAttributes = Optional<auth_permissionAttributes, auth_permissionOptionalAttributes>;

export class auth_permission extends Model<auth_permissionAttributes, auth_permissionCreationAttributes> implements auth_permissionAttributes {
  id!: number;
  name!: string;
  content_type_id!: number;
  codename!: string;

  // auth_permission hasMany auth_group_permissions via permission_id
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
  // auth_permission hasMany auth_user_user_permissions via permission_id
  auth_user_user_permissions!: auth_user_user_permissions[];
  getAuth_user_user_permissions!: Sequelize.HasManyGetAssociationsMixin<auth_user_user_permissions>;
  setAuth_user_user_permissions!: Sequelize.HasManySetAssociationsMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  addAuth_user_user_permission!: Sequelize.HasManyAddAssociationMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  addAuth_user_user_permissions!: Sequelize.HasManyAddAssociationsMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  createAuth_user_user_permission!: Sequelize.HasManyCreateAssociationMixin<auth_user_user_permissions>;
  removeAuth_user_user_permission!: Sequelize.HasManyRemoveAssociationMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  removeAuth_user_user_permissions!: Sequelize.HasManyRemoveAssociationsMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  hasAuth_user_user_permission!: Sequelize.HasManyHasAssociationMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  hasAuth_user_user_permissions!: Sequelize.HasManyHasAssociationsMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  countAuth_user_user_permissions!: Sequelize.HasManyCountAssociationsMixin;
  // auth_permission belongsTo django_content_type via content_type_id
  content_type!: django_content_type;
  getContent_type!: Sequelize.BelongsToGetAssociationMixin<django_content_type>;
  setContent_type!: Sequelize.BelongsToSetAssociationMixin<django_content_type, django_content_typeId>;
  createContent_type!: Sequelize.BelongsToCreateAssociationMixin<django_content_type>;

  static initModel(sequelize: Sequelize.Sequelize): typeof auth_permission {
    return auth_permission.init({
    id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    name: {
      type: DataTypes.STRING(255),
      allowNull: false
    },
    content_type_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'django_content_type',
        key: 'id'
      }
    },
    codename: {
      type: DataTypes.STRING(100),
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'auth_permission',
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
        name: "auth_permission_content_type_id_codename_01ab375a_uniq",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "content_type_id" },
          { name: "codename" },
        ]
      },
    ]
  });
  }
}
