import * as Yup from 'yup';

export const registerSchema = Yup.object({
  firstName: Yup.string()
    .max(30, 'Must be 30 characters or less')
    .min(2, 'Must be 2 characters or more')
    .required('Required'),
  lastName: Yup.string()
    .max(30, 'Must be 30 characters or less')
    .min(2, 'Must be 2 characters or more')
    .required('Required'),
  username: Yup.string()
    .max(32, 'Must be 32 characters or less')
    .min(3, 'Must be 3 characters or more')
    .required('Required'),
  email: Yup.string().email('Invalid email adress').required('Required'),
});
