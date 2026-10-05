import { Container, Input, Main, Form, Button, FormTitle } from '../../components'
import styles from './styles.module.css'
import { useFormWithValidation } from '../../utils'
import MetaTags from 'react-meta-tags'
import { AuthContext } from '../../contexts'
import { useContext } from 'react'
import { Redirect } from 'react-router-dom'

const ResetPassword = ({ onPasswordReset }) => {
  const { values, handleChange, isValid, resetForm } = useFormWithValidation()
  const authContext = useContext(AuthContext)

  {authContext && <Redirect to='/recipes' />}

  return <Main withBG asFlex>
    <Container className={styles.center}>
      <MetaTags>
        <title>Sign in</title>
        <meta name="description" content="Foodgram - Password reset" />
        <meta property="og:title" content="Password reset" />
      </MetaTags>
      <Form
        className={styles.form}
        onSubmit={e => {
          e.preventDefault()
          onPasswordReset(values)
        }}
      >
        <FormTitle>Password reset</FormTitle>

        <Input
          required
          name='email'
          placeholder='Email'
          onChange={handleChange}
        />
        <Button
          modifier='style_dark'
          disabled={!isValid}
          type='submit'
          className={styles.button}
        >
          Reset
        </Button>
      </Form>
    </Container>
  </Main>
}

export default ResetPassword
