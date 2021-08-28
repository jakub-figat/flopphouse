import { RegisterFormWrapper, Form, RegisterHeader, SubmitButton } from './styles';
import { Formik } from 'formik';
import { registerSchema } from '../../../config/validationSchema';
import { RegisterValidation } from '../../models/index';
import TextInput from './TextInput';

const RegisterForm = () => {
  return (
    <RegisterFormWrapper>
      <RegisterHeader>Sign in to flopphouse</RegisterHeader>
      <Formik
        initialValues={{
          firstName: '',
          lastName: '',
          username: '',
          email: '',
          password: '',
        }}
        validationSchema={registerSchema}
        onSubmit={values => {
          alert(JSON.stringify(values, null, 2));
        }}
      >
        {formik => (
          <Form onSubmit={formik.handleSubmit}>
            <TextInput label="First name" name="firstName" type="text" placeholder="First name" />
            <TextInput label="Last name" name="lastName" type="text" placeholder="Last name" />
            <TextInput label="Username" name="username" type="text" placeholder="Username" />
            <TextInput label="Email" name="email" type="text" placeholder="Email" />
            <TextInput label="Password" name="password" type="password" placeholder="Password" />
            <SubmitButton type="submit">Sign up</SubmitButton>
          </Form>
        )}
      </Formik>
    </RegisterFormWrapper>
  );
};

export default RegisterForm;
