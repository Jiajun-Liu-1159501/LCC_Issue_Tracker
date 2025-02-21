from loginapp.constant.user_role import Role


print(Role.of('VISITOR').get_allowed_operations())