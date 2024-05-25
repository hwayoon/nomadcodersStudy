export default function Tabs({ children, buttons, buttonsConatiner = "menu" }) {
  const ButtonsConatiner = buttonsConatiner;
  return (
    <>
      <ButtonsConatiner>{buttons}</ButtonsConatiner>
      {children}
    </>
  );
}
