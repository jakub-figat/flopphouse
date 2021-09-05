import styled from 'styled-components';

import SVG from 'react-inlinesvg';

import { colors } from '../../../config/stylesConfig';

export const PageWrapper = styled.div`
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
    'Open Sans', 'Helvetica Neue', sans-serif;
`;

export const CaracalLogo = styled(SVG)`
  width: 3rem;
  height: 3rem;
  position: absolute;
  top: 0;
  margin-top: 5px;

  & path {
    fill: ${colors.yellowTheme};
  }
`;
