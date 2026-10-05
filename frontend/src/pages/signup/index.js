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
import { Redirect } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../../contexts";
import MetaTags from "react-meta-tags";

const SignUp = ({ onSignUp, submitError, setSubmitError }) => {
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
          <title>Sign up</title>
          <meta
            name="description"
            content="Foodgram - Sign up"
          />
          <meta property="og:title" content="Sign up" />
        </MetaTags>
        <Form
          className={styles.form}
          onSubmit={(e) => {
            e.preventDefault();
            onSignUp(values);
          }}
        >
          <FormTitle>Sign up</FormTitle>
          <Input
            placeholder="First name"
            name="first_name"
            required
            isAuth={true}
            error={errors}
            onChange={onChange}
          />
          <Input
            placeholder="Last name"
            name="last_name"
            required
            isAuth={true}
            error={errors}
            onChange={onChange}
          />
          <Input
            placeholder="Username"
            name="username"
            required
            isAuth={true}
            error={errors}
            onChange={onChange}
          />

          <Input
            placeholder="Email address"
            name="email"
            required
            isAuth={true}
            error={errors}
            onChange={onChange}
          />
          <Input
            placeholder="Password"
            type="password"
            name="password"
            required
            isAuth={true}
            error={errors}
            submitError={submitError}
            onChange={onChange}
          />
          <Button modifier="style_dark" type="submit" className={styles.button}>
            Create account
          </Button>
        </Form>
      </Container>
    </Main>
  );
};

export default SignUp;
