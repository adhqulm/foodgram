import {
  Container,
  Input,
  FormTitle,
  Main,
  Form,
  Button,
} from "../../components";
import styles from "./styles.module.css";
import { useFormWithValidation } from "../../utils";
import { AuthContext } from "../../contexts";
import { Redirect } from "react-router-dom";
import { useContext } from "react";
import MetaTags from "react-meta-tags";
import { ChangePasswordText } from "../../components/change-password-text";

const ChangePassword = ({ onPasswordChange, submitError, setSubmitError }) => {
  const { values, handleChange, errors, isValid, resetForm } =
    useFormWithValidation();
  const authContext = useContext(AuthContext);

  const onChange = (e) => {
    setSubmitError({ submitError: "" });
    handleChange(e);
  };

  return (
    <Main withBG asFlex>
      <Container className={styles.center}>
        <MetaTags>
          <title>Change password</title>
          <meta
            name="description"
            content="Foodgram - Change password"
          />
          <meta property="og:title" content="Change password" />
        </MetaTags>
        <Form
          className={styles.form}
          onSubmit={(e) => {
            e.preventDefault();
            onPasswordChange(values);
          }}
        >
          <FormTitle>Change password</FormTitle>
          <Input
            required
            isAuth={true}
            placeholder="Old password"
            type="password"
            name="current_password"
            error={errors}
            onChange={onChange}
          />
          <Input
            required
            isAuth={true}
            placeholder="New password"
            type="password"
            name="new_password"
            error={errors}
            onChange={onChange}
          />
          <ul className={styles.texts}>
            <li className={styles.text}>
              <ChangePasswordText text="Your password can't be too similar to your name or other personal information" />
            </li>
            <li className={styles.text}>
              <ChangePasswordText text="Your password must contain at least 8 characters" />
            </li>
            <li className={styles.text}>
              <ChangePasswordText text="Your password can't be a commonly used password" />
            </li>
            <li className={styles.text}>
              <ChangePasswordText text="Your password can't be entirely numeric" />
            </li>
          </ul>
          <Input
            required
            isAuth={true}
            placeholder="Confirm new password"
            type="password"
            name="repeat_password"
            error={errors}
            submitError={submitError}
            onChange={onChange}
          />
          <Button
            modifier="style_dark"
            type="submit"
            className={styles.button}
            disabled={
              !isValid || values.new_password !== values.repeat_password
            }
          >
            Change password
          </Button>
        </Form>
      </Container>
    </Main>
  );
};

export default ChangePassword;
