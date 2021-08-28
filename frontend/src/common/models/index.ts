export interface RegisterValidation {
  firstName: string;
  lastName: string;
  username: string;
  email: string;
}

export interface TextInputProps {
  label: string;
  name: string;
  type: string;
  placeholder?: string;
}
