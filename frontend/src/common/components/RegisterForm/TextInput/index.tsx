import { useField } from 'formik';
import { TextInputProps } from '../../../models/index';

import { InputLabel, Input } from './styles';
import { ErrorMessage } from '../styles';

const TextInput: React.FC<TextInputProps> = ({ label, ...props }) => {
  const [field, meta] = useField(props);

  return (
    <>
      <InputLabel htmlFor={props.name}>{label}</InputLabel>
      <Input {...field} {...props} />
      {meta.touched && meta.error ? <ErrorMessage>{meta.error}</ErrorMessage> : null}
    </>
  );
};

export default TextInput;
