import * as Yup from 'yup';

export const registerSchema = Yup.object({
  firstName: Yup.string()
    .min(2, 'Must be 2 characters or more')
    .max(30, 'Must be 30 characters or less')
    .required('Required'),
  lastName: Yup.string()
    .min(2, 'Must be 2 characters or more')
    .max(30, 'Must be 30 characters or less')
    .required('Required'),
  username: Yup.string()
    .min(3, 'Must be 3 characters or more')
    .max(30, 'Must be 30 characters or less')
    .required('Required'),
  email: Yup.string().email('Invalid email adress').required('Required'),
  password: Yup.string()
    .min(8, 'Must be 8 characters or more')
    .max(32, 'Must be 32 characters or less')
    .required('Required'),
});
