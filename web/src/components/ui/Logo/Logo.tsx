/* eslint-disable react/require-default-props */
import Link from 'next/link';
import { FC } from 'react';
import styles from './Logo.module.css';
import t from '~/locales/_ja';

const Logo: FC = () => {

  return (
    <Link href="/">
      <div className={`${styles.logo}`} id="logo">
        <span>📚</span>
        <span>{t.TITLE}</span>
      </div>
    </Link>
  );
};

export default Logo;
