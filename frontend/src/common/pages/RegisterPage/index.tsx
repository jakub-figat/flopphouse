import { PageWrapper, CaracalLogo } from './styles';

import RegisterForm from '../../components/RegisterForm';
import CaracalIcon from '../../../assets/images/caracal-logo.svg';

const RegisterPage = () => {
  return (
    <PageWrapper>
      <CaracalLogo src={CaracalIcon} />
      <RegisterForm />
    </PageWrapper>
  );
};

export default RegisterPage;
