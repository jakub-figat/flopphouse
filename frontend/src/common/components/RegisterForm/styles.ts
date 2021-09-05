import styled from 'styled-components';

import { fontSize, colors, fontWeight } from '../../../config/stylesConfig';

export const RegisterFormWrapper = styled.div`
  height: 550px;

  width: 300px;
`;

export const Form = styled.form`
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: space-evenly;
`;

export const RegisterHeader = styled.h3`
  font-size: ${fontSize.large};
  color: ${colors.darkBackground};
  font-weight: ${fontWeight.heavy};
`;

export const RegisterHeaderWrapper = styled.span`
  color: ${colors.yellowTheme};
`;

export const ErrorMessage = styled.div`
  color: ${colors.errorMessage};
`;

export const SubmitButton = styled.button`
  margin-top: 20px;
  display: inline-block;
  outline: none;
  color: ${colors.whiteText};
  cursor: pointer;
  font-size: 16px;
  line-height: 20px;
  font-weight: ${fontWeight.semiBold};
  border-radius: 8px;
  padding: 14px 24px;
  border: none;
  background: linear-gradient(
    to right,
    rgb(230, 30, 77) 0%,
    rgb(227, 28, 95) 50%,
    rgb(215, 4, 102) 100%
  );
`;
