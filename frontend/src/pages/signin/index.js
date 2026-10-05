import {
  Container,
  Input,
  Main,
  Form,
  Button,
  FormTitle,
} from "../../components";
import styles from "./styles.module.css";
import { useFormWithValidation } from "../../utils";
import { AuthContext } from "../../contexts";
import { Redirect } from "react-router-dom";
import { useContext } from "react";
import MetaTags from "react-meta-tags";

const SignIn = ({ onSignIn, submitError, setSubmitError }) => {
  const { values, handleChange, errors } = useFormWithValidation();
  const authContext = useContext(AuthContext);

  const onChange = (e) => {
    setSubmitError({ submitError: "" });
    handleChange(e);
  };

  return (
    <Main withBG asFlex>
      {authContext && <Redirect to="/recipes" />}
      <Container className={styles.center}>
        <MetaTags>
          <title>Sign in</title>
          <meta
            name="description"
            content="Foodgram - Sign in"
          />
          <meta property="og:title" content="Sign in" />
        </MetaTags>
        <Form
          className={styles.form}
          onSubmit={(e) => {
            e.preventDefault();
            onSignIn(values);
          }}
        >
          <FormTitle>Sign in</FormTitle>

          <Input
            required
            isAuth={true}
            name="email"
            placeholder="Email"
            onChange={onChange}
            error={errors}
          />
          <Input
            required
            isAuth={true}
            type="password"
            name="password"
            placeholder="Password"
            error={errors}
            submitError={submitError}
            onChange={onChange}
          />
          {/* <LinkComponent
            className={styles.link}
            href="/reset-password"
            title="Forgot your password?"
          /> */}
          <Button modifier="style_dark" type="submit" className={styles.button}>
            Sign in
          </Button>
        </Form>
      </Container>
    </Main>
  );
};

export default SignIn;
