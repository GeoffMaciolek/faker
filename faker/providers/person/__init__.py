from .. import BaseProvider

localized = True


class Provider(BaseProvider):
    formats = ['{{first_name}} {{last_name}}']

    first_names = ['John', 'Jane']

    last_names = ['Doe']

    # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    language_names = [
        'Afar', 'Abkhazian', 'Avestan', 'Afrikaans', 'Akan', 'Amharic',
        'Aragonese', 'Arabic', 'Assamese', 'Avaric', 'Aymara', 'Azerbaijani',
        'Bashkir', 'Belarusian', 'Bulgarian', 'Bihari languages', 'Bislama',
        'Bambara', 'Bengali', 'Tibetan', 'Breton', 'Bosnian', 'Catalan',
        'Chechen', 'Chamorro', 'Corsican', 'Cree', 'Czech', 'Church Slavic',
        'Chuvash', 'Welsh', 'Danish', 'German', 'Divehi', 'Dzongkha', 'Ewe',
        'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Basque',
        'Persian', 'Fulah', 'Finnish', 'Fijian', 'Faroese', 'French',
        'Western Frisian', 'Irish', 'Gaelic', 'Galician', 'Guarani',
        'Gujarati', 'Manx', 'Hausa', 'Hebrew', 'Hindi', 'Hiri Motu',
        'Croatian', 'Haitian', 'Hungarian', 'Armenian', 'Herero',
        'Interlingua', 'Indonesian', 'Interlingue', 'Igbo', 'Sichuan Yi',
        'Inupiaq', 'Ido', 'Icelandic', 'Italian', 'Inuktitut', 'Japanese',
        'Javanese', 'Georgian', 'Kongo', 'Kikuyu', 'Kuanyama', 'Kazakh',
        'Kalaallisut', 'Central Khmer', 'Kannada', 'Korean', 'Kanuri',
        'Kashmiri', 'Kurdish', 'Komi', 'Cornish', 'Kirghiz', 'Latin',
        'Luxembourgish', 'Ganda', 'Limburgan', 'Lingala', 'Lao', 'Lithuanian',
        'Luba-Katanga', 'Latvian', 'Malagasy', 'Marshallese', 'Maori',
        'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese',
        'Burmese', 'Nauru', 'North Ndebele', 'Nepali',
        'Ndonga', 'Dutch', 'Norwegian Nynorsk', 'Norwegian', 'South Ndebele',
        'Navajo', 'Chichewa', 'Occitan', 'Ojibwa', 'Oromo', 'Oriya',
        'Ossetian', 'Panjabi', 'Pali', 'Polish', 'Pushto', 'Portuguese',
        'Quechua', 'Romansh', 'Rundi', 'Romanian', 'Russian', 'Kinyarwanda',
        'Sanskrit', 'Sardinian', 'Sindhi', 'Northern Sami', 'Sango', 'Sinhala',
        'Slovak', 'Slovenian', 'Samoan', 'Shona', 'Somali', 'Albanian',
        'Serbian', 'Swati', 'Sotho, Southern', 'Sundanese', 'Swedish',
        'Swahili', 'Tamil', 'Telugu', 'Tajik', 'Thai', 'Tigrinya', 'Turkmen',
        'Tagalog', 'Tswana', 'Tonga', 'Turkish', 'Tsonga', 'Tatar', 'Twi',
        'Tahitian', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Venda',
        'Vietnamese', 'Walloon', 'Wolof', 'Xhosa', 'Yiddish',
        'Yoruba', 'Zhuang', 'Chinese', 'Zulu',
    ]

    def name(self):
        """
        :example 'John Doe'
        """
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)

    def first_name(self):
        return self.random_element(self.first_names)

    def last_name(self):
        return self.random_element(self.last_names)

    def name_male(self):
        if hasattr(self, 'formats_male'):
            formats = self.formats_male
        else:
            formats = self.formats
        pattern = self.random_element(formats)
        return self.generator.parse(pattern)

    def name_nonbinary(self):
        if hasattr(self, 'formats_nonbinary'):
            formats = self.formats_nonbinary
        else:
            formats = self.formats
        pattern = self.random_element(formats)
        return self.generator.parse(pattern)

    def name_female(self):
        if hasattr(self, 'formats_female'):
            formats = self.formats_female
        else:
            formats = self.formats
        pattern = self.random_element(formats)
        return self.generator.parse(pattern)

    def first_name_male(self):
        if hasattr(self, 'first_names_male'):
            return self.random_element(self.first_names_male)
        return self.first_name()

    def first_name_nonbinary(self):
        if hasattr(self, 'first_names_nonbinary'):
            return self.random_element(self.first_names_nonbinary)
        return self.first_name()

    def first_name_female(self):
        if hasattr(self, 'first_names_female'):
            return self.random_element(self.first_names_female)
        return self.first_name()

    def first_name_abbreviated(self, first_name: str = None, length: int = 1, add_period: bool = False):
        """Generate an abbreviated first name

        This returns only a first initial by default, but optionally allows the
        use of a specific name, choosing the number of first (or last)
        characters, and adding a period to the end.

        In general, using e.g. ``?`` in ``bothify()`` will meet most needs, but
        this keeps the letters within the expected ranges (if ever relevant),
        and also allows for overriding of the selected name, for ``user_name()``
        and similar functions.

        Args:
            first_name (:obj:`str`, optional): A first name to override with; by
                default, this is generated by ``first_name()`` by default.
            length (:obj:`int`, optional): How many characters to use. Defaults to 1.
                To get the LAST x characters, specify a negative number.
            add_period (bool, optional): Add a period, returning (for example).
                'I.'; Defaults to False.

        Returns:
            str: the abbreviated name
        """

        if not first_name:  # We'll use a random first name if so desired.
            first_name = self.first_name()

        # Have we been given a reasonable length input? if not, use default (1)
        if type(length) == str:
            if not length.isdigit():
                if length[0] == '-' and length[1:].isdigit():
                    length = int(length)
                else:
                    length = 1
            else:
                length = int(length)
        elif type(length) != int or length == 0:
            length = 1
        if length > 0:  # Getting the first X chars
            slice_start = None
            # Sanity check - don't get the first 8 chars of a 2 char. name.
            slice_end = min(abs(length), len(first_name))
        else:  # Negative number - get the *last* X chars (and sanity check)
            slice_start = -1 * min(abs(length), len(first_name))
            slice_end = None

        name_result = first_name[slice_start:slice_end]  # Do slice/abbreviate

        if add_period:
            name_result += '.'
        return name_result

    def last_name_male(self):
        if hasattr(self, 'last_names_male'):
            return self.random_element(self.last_names_male)
        return self.last_name()

    def last_name_nonbinary(self):
        if hasattr(self, 'last_names_nonbinary'):
            return self.random_element(self.last_names_nonbinary)
        return self.last_name()

    def last_name_female(self):
        if hasattr(self, 'last_names_female'):
            return self.random_element(self.last_names_female)
        return self.last_name()

    def prefix(self):
        if hasattr(self, 'prefixes'):
            return self.random_element(self.prefixes)
        if hasattr(self, 'prefixes_male') and hasattr(self, 'prefixes_female') and hasattr(self, 'prefixes_nonbinary'):
            prefixes = self.random_element(
                (self.prefixes_male, self.prefixes_female, self.prefixes_nonbinary))
            return self.random_element(prefixes)
        if hasattr(self, 'prefixes_male') and hasattr(self, 'prefixes_female'):
            prefixes = self.random_element(
                (self.prefixes_male, self.prefixes_female))
            return self.random_element(prefixes)
        return ''

    def prefix_male(self):
        if hasattr(self, 'prefixes_male'):
            return self.random_element(self.prefixes_male)
        return self.prefix()

    def prefix_nonbinary(self):
        if hasattr(self, 'prefixes_nonbinary'):
            return self.random_element(self.prefixes_nonbinary)
        return self.prefix()

    def prefix_female(self):
        if hasattr(self, 'prefixes_female'):
            return self.random_element(self.prefixes_female)
        return self.prefix()

    def suffix(self):
        if hasattr(self, 'suffixes'):
            return self.random_element(self.suffixes)
        if hasattr(self, 'suffixes_male') and hasattr(self, 'suffixes_female') and hasattr(self, 'suffixes_nonbinary'):
            suffixes = self.random_element(
                (self.suffixes_male, self.suffixes_female, self.suffixes_nonbinary))
            return self.random_element(suffixes)
        if hasattr(self, 'suffixes_male') and hasattr(self, 'suffixes_female'):
            suffixes = self.random_element(
                (self.suffixes_male, self.suffixes_female))
            return self.random_element(suffixes)
        return ''

    def suffix_male(self):
        if hasattr(self, 'suffixes_male'):
            return self.random_element(self.suffixes_male)
        return self.suffix()

    def suffix_nonbinary(self):
        if hasattr(self, 'suffixes_nonbinary'):
            return self.random_element(self.suffixes_nonbinary)
        return self.suffix()

    def suffix_female(self):
        if hasattr(self, 'suffixes_female'):
            return self.random_element(self.suffixes_female)
        return self.suffix()

    def language_name(self):
        """Generate a random i18n language name (e.g. English)."""
        return self.random_element(self.language_names)
