export default function Header({ children }) {
  return (
    <header id="header">
      <img src="src\assets\investment-calculator-logo.png" />
      {children}
    </header>
  );
}
